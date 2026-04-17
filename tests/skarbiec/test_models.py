import pytest
from skarbiec.models import (
    User, Konto, CelSkladkowy, CelSkladkowyPlatnik, Transakcja,
    PrzypisaniePlatnosci, ImportSesja, CelStatus, PlatnikStatus,
    DopasowanieStatus, ImportStatus
)


@pytest.mark.django_db
class TestKontoModel:

    def test_konto_create_with_required_fields(self, member_user):
        konto = Konto.objects.create(
            user=member_user,
            numer_konta="12345678901234567890",
            numer_telefonu="+48123456789",
            nazwa_wlasciciela="Jan Kowalski",
        )
        assert konto.id is not None
        assert konto.user == member_user
        assert konto.numer_konta == "12345678901234567890"

    def test_user_can_have_multiple_accounts(self, member_user):
        Konto.objects.create(
            user=member_user,
            numer_konta="11111111111111111111",
            numer_telefonu="+48111111111",
            nazwa_wlasciciela="Jan",
        )
        Konto.objects.create(
            user=member_user,
            numer_konta="22222222222222222222",
            numer_telefonu="+48222222222",
            nazwa_wlasciciela="Jan",
        )

        accounts = Konto.objects.filter(user=member_user)
        assert accounts.count() == 2

    def test_find_konto_by_account_number(self, konto):
        found = Konto.objects.get(numer_konta=konto.numer_konta)
        assert found.id == konto.id

    def test_konto_phone_number_format(self, konto):
        assert konto.numer_telefonu.startswith("+48")


@pytest.mark.django_db
class TestCelSkladkowyModel:

    def test_cel_skladkowy_create_with_required_fields(self):
        cel = CelSkladkowy.objects.create(
            tytul="Collection Goal",
            opis="Test goal",
            termin="2025-12-31",
            kod="TEST001",
            status=CelStatus.OPEN,
        )
        assert cel.id is not None
        assert cel.tytul == "Collection Goal"
        assert cel.status == CelStatus.OPEN

    def test_cel_skladkowy_created_at_is_set(self):
        cel = CelSkladkowy.objects.create(
            tytul="Goal",
            opis="Test",
            termin="2025-12-31",
            kod="CODE1",
        )
        assert cel.data_utworzenia is not None

    def test_cel_skladkowy_default_status_open(self):
        cel = CelSkladkowy.objects.create(
            tytul="Goal",
            opis="Test",
            termin="2025-12-31",
            kod="CODE1",
        )
        assert cel.status == CelStatus.OPEN

    def test_cel_skladkowy_status_transitions(self, cel_skladkowy):
        cel_skladkowy.status = CelStatus.CLOSED
        cel_skladkowy.save()

        updated = CelSkladkowy.objects.get(id=cel_skladkowy.id)
        assert updated.status == CelStatus.CLOSED

    def test_cel_skladkowy_has_platnicy(self, multiple_platnicy):
        assert len(multiple_platnicy) > 0
        cel = multiple_platnicy[0].cel_skladkowy
        assert cel.platnicy.count() >= 1

    def test_find_cel_by_kod(self, cel_skladkowy):
        found = CelSkladkowy.objects.get(kod=cel_skladkowy.kod)
        assert found.id == cel_skladkowy.id


@pytest.mark.django_db
class TestCelSkladkowyPlatnikModel:

    def test_cel_platnik_create_with_required_fields(self, cel_skladkowy, member_user):
        platnik = CelSkladkowyPlatnik.objects.create(
            cel_skladkowy=cel_skladkowy,
            platnik=member_user,
            kwota_docelowa=100.00,
            kwota_zaplacona=0.00,
            status=PlatnikStatus.NIEZAPLACONE,
        )
        assert platnik.id is not None
        assert platnik.kwota_docelowa == 100.00
        assert platnik.status == PlatnikStatus.NIEZAPLACONE

    def test_cel_platnik_tracks_paid_amount(self, cel_platnik):
        cel_platnik.kwota_zaplacona = 50.00
        cel_platnik.save()

        updated = CelSkladkowyPlatnik.objects.get(id=cel_platnik.id)
        assert updated.kwota_zaplacona == 50.00

    def test_cel_platnik_status_transitions(self, cel_platnik):
        cel_platnik.status = PlatnikStatus.CZESCIOWO
        cel_platnik.save()

        assert cel_platnik.status == PlatnikStatus.CZESCIOWO

    def test_cel_platnik_mark_fully_paid(self, cel_platnik):
        cel_platnik.kwota_zaplacona = cel_platnik.kwota_docelowa
        cel_platnik.status = PlatnikStatus.OPLACONE
        cel_platnik.save()

        updated = CelSkladkowyPlatnik.objects.get(id=cel_platnik.id)
        assert updated.status == PlatnikStatus.OPLACONE

    def test_multiple_users_same_goal(self, cel_skladkowy, member_user, member_user_2):
        platnik1 = CelSkladkowyPlatnik.objects.create(
            cel_skladkowy=cel_skladkowy,
            platnik=member_user,
            kwota_docelowa=100.00,
            kwota_zaplacona=0.00,
        )
        platnik2 = CelSkladkowyPlatnik.objects.create(
            cel_skladkowy=cel_skladkowy,
            platnik=member_user_2,
            kwota_docelowa=100.00,
            kwota_zaplacona=0.00,
        )

        goal_platnicy = cel_skladkowy.platnicy.all()
        assert goal_platnicy.count() >= 2


@pytest.mark.django_db
class TestTransakcjaModel:

    def test_transakcja_create_with_required_fields(self, konto):
        tx = Transakcja.objects.create(
            data="2025-01-15",
            kwota=100.00,
            tytul="Transfer TEST001",
            nr_konta=konto.numer_konta,
            nadawca="Jan Kowalski",
        )
        assert tx.id is not None
        assert tx.kwota == 100.00
        assert tx.nr_konta == konto.numer_konta

    def test_transakcja_can_be_matched_to_konto(self, transakcja, konto):
        assert transakcja.nr_konta == konto.numer_konta

    def test_find_transakcja_by_account(self, transakcja, konto):
        txs = Transakcja.objects.filter(nr_konta=konto.numer_konta)
        assert txs.count() > 0

    def test_transakcja_stores_sender_info(self, transakcja):
        assert transakcja.nadawca == "Jan Kowalski"


@pytest.mark.django_db
class TestPrzypisaniePlatnosciModel:

    def test_przypisanie_create_with_required_fields(self, transakcja, cel_skladkowy, cel_platnik):
        przypisanie = PrzypisaniePlatnosci.objects.create(
            transakcja=transakcja,
            cel_skladkowy=cel_skladkowy,
            cel_platnik=cel_platnik,
            kwota_przypisana=100.00,
            status_dopasowania=DopasowanieStatus.AUTO,
        )
        assert przypisanie.id is not None
        assert przypisanie.kwota_przypisana == 100.00
        assert przypisanie.status_dopasowania == DopasowanieStatus.AUTO

    def test_przypisanie_status_auto(self, transakcja, cel_skladkowy, cel_platnik):
        przypisanie = PrzypisaniePlatnosci.objects.create(
            transakcja=transakcja,
            cel_skladkowy=cel_skladkowy,
            cel_platnik=cel_platnik,
            kwota_przypisana=50.00,
            status_dopasowania=DopasowanieStatus.AUTO,
        )
        assert przypisanie.status_dopasowania == DopasowanieStatus.AUTO

    def test_przypisanie_status_manual(self, transakcja, cel_skladkowy, cel_platnik):
        przypisanie = PrzypisaniePlatnosci.objects.create(
            transakcja=transakcja,
            cel_skladkowy=cel_skladkowy,
            cel_platnik=cel_platnik,
            kwota_przypisana=50.00,
            status_dopasowania=DopasowanieStatus.MANUAL,
        )
        assert przypisanie.status_dopasowania == DopasowanieStatus.MANUAL

    def test_przypisanie_status_uncertain(self, transakcja, cel_skladkowy, cel_platnik):
        przypisanie = PrzypisaniePlatnosci.objects.create(
            transakcja=transakcja,
            cel_skladkowy=cel_skladkowy,
            cel_platnik=cel_platnik,
            kwota_przypisana=50.00,
            status_dopasowania=DopasowanieStatus.NIEPEWNE,
        )
        assert przypisanie.status_dopasowania == DopasowanieStatus.NIEPEWNE

    def test_przypisanie_data_przypisania_set(self, transakcja, cel_skladkowy, cel_platnik):
        przypisanie = PrzypisaniePlatnosci.objects.create(
            transakcja=transakcja,
            cel_skladkowy=cel_skladkowy,
            cel_platnik=cel_platnik,
            kwota_przypisana=50.00,
            status_dopasowania=DopasowanieStatus.AUTO,
        )
        assert przypisanie.data_przypisania is not None


@pytest.mark.django_db
class TestImportSesjaModel:

    def test_import_sesja_create_with_required_fields(self):
        sesja = ImportSesja.objects.create(
            data_importu="2025-01-15",
            nazwa_pliku="transactions.csv",
            status=ImportStatus.SUCCESS,
        )
        assert sesja.id is not None
        assert sesja.nazwa_pliku == "transactions.csv"
        assert sesja.status == ImportStatus.SUCCESS

    def test_import_sesja_status_success(self):
        sesja = ImportSesja.objects.create(
            data_importu="2025-01-15",
            nazwa_pliku="data.csv",
            status=ImportStatus.SUCCESS,
        )
        assert sesja.status == ImportStatus.SUCCESS

    def test_import_sesja_status_failed(self):
        sesja = ImportSesja.objects.create(
            data_importu="2025-01-15",
            nazwa_pliku="data.csv",
            status=ImportStatus.FAILED,
        )
        assert sesja.status == ImportStatus.FAILED

    def test_import_sesja_status_partial(self):
        sesja = ImportSesja.objects.create(
            data_importu="2025-01-15",
            nazwa_pliku="data.csv",
            status=ImportStatus.PARTIAL,
        )
        assert sesja.status == ImportStatus.PARTIAL

    def test_import_sesja_has_transactions(self, import_sesja, transakcja):
        transakcja.import_sesja = import_sesja
        transakcja.save()

        txs = import_sesja.transakcje.all()
        assert txs.count() > 0

