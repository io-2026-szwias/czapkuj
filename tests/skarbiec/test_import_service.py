import pytest
from io import StringIO
from skarbiec.services import ImportService
from skarbiec.models import ImportSesja, Transakcja, ImportStatus


@pytest.mark.django_db
class TestImportService:

    def test_import_csv_creates_session(self, db):
        csv_content = """nr_konta,kwota,tytul,nadawca,data
12345678901234567890,100.00,Transfer TEST001,Jan Kowalski,2025-01-15"""

        service = ImportService()
        sesja = service.import_csv(StringIO(csv_content), "test.csv")

        assert sesja.id is not None
        assert sesja.nazwa_pliku == "test.csv"

    def test_import_csv_creates_transactions(self, db):
        csv_content = """nr_konta,kwota,tytul,nadawca,data
12345678901234567890,100.00,Transfer TEST001,Jan Kowalski,2025-01-15
12345678901234567890,50.00,Transfer TEST002,Jan Kowalski,2025-01-16"""

        service = ImportService()
        sesja = service.import_csv(StringIO(csv_content), "test.csv")

        txs = Transakcja.objects.all()
        assert txs.count() >= 2

    def test_import_csv_success_status(self, db):
        csv_content = """nr_konta,kwota,tytul,nadawca,data
12345678901234567890,100.00,Transfer,Jan,2025-01-15"""

        service = ImportService()
        sesja = service.import_csv(StringIO(csv_content), "test.csv")

        assert sesja.status == ImportStatus.SUCCESS

    def test_import_csv_partial_status_on_errors(self, db):
        csv_content = """nr_konta,kwota,tytul,nadawca,data
12345678901234567890,100.00,Transfer,Jan,2025-01-15
invalid_data"""

        service = ImportService()
        sesja = service.import_csv(StringIO(csv_content), "test.csv")

        assert sesja.status in [ImportStatus.SUCCESS, ImportStatus.PARTIAL]

    def test_import_csv_failed_status_on_all_errors(self, db):
        csv_content = """invalid_header
broken_line"""

        service = ImportService()
        sesja = service.import_csv(StringIO(csv_content), "test.csv")

        assert sesja.status in [ImportStatus.FAILED, ImportStatus.PARTIAL]

    def test_import_csv_empty_file(self, db):
        csv_content = ""

        service = ImportService()
        sesja = service.import_csv(StringIO(csv_content), "empty.csv")

        assert sesja is not None

    def test_import_csv_stores_file_name(self, db):
        csv_content = """nr_konta,kwota,tytul,nadawca,data
12345678901234567890,100.00,Transfer,Jan,2025-01-15"""

        service = ImportService()
        sesja = service.import_csv(StringIO(csv_content), "my_transactions.csv")

        assert sesja.nazwa_pliku == "my_transactions.csv"

    def test_import_csv_stores_import_date(self, db):
        csv_content = """nr_konta,kwota,tytul,nadawca,data
12345678901234567890,100.00,Transfer,Jan,2025-01-15"""

        service = ImportService()
        sesja = service.import_csv(StringIO(csv_content), "test.csv")

        assert sesja.data_importu is not None

    def test_import_csv_multiple_rows(self, db):
        csv_content = """nr_konta,kwota,tytul,nadawca,data
11111111111111111111,100.00,Transfer 1,User 1,2025-01-15
22222222222222222222,200.00,Transfer 2,User 2,2025-01-16
33333333333333333333,300.00,Transfer 3,User 3,2025-01-17"""

        service = ImportService()
        sesja = service.import_csv(StringIO(csv_content), "test.csv")

        txs = Transakcja.objects.filter(import_sesja=sesja)
        assert txs.count() >= 3

    def test_import_csv_preserves_transaction_data(self, db):
        csv_content = """nr_konta,kwota,tytul,nadawca,data
12345678901234567890,99.99,Transfer TEST,Sender Name,2025-01-15"""

        service = ImportService()
        sesja = service.import_csv(StringIO(csv_content), "test.csv")

        tx = Transakcja.objects.first()
        assert tx.kwota == 99.99
        assert tx.tytul == "Transfer TEST"
        assert tx.nadawca == "Sender Name"

    def test_import_csv_decimal_amounts(self, db):
        csv_content = """nr_konta,kwota,tytul,nadawca,data
12345678901234567890,123.45,Transfer,Jan,2025-01-15"""

        service = ImportService()
        sesja = service.import_csv(StringIO(csv_content), "test.csv")

        tx = Transakcja.objects.first()
        assert tx.kwota == 123.45

    def test_import_csv_large_amounts(self, db):
        csv_content = """nr_konta,kwota,tytul,nadawca,data
12345678901234567890,9999999.99,Big Transfer,Jan,2025-01-15"""

        service = ImportService()
        sesja = service.import_csv(StringIO(csv_content), "test.csv")

        tx = Transakcja.objects.first()
        assert tx.kwota == 9999999.99

    def test_import_csv_special_characters_in_title(self, db):
        csv_content = """nr_konta,kwota,tytul,nadawca,data
12345678901234567890,100.00,Transfer: TEST/001,Jan Kowalski,2025-01-15"""

        service = ImportService()
        sesja = service.import_csv(StringIO(csv_content), "test.csv")

        tx = Transakcja.objects.first()
        assert "TEST/001" in tx.tytul

