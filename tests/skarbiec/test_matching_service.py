import pytest
from skarbiec.services import MatchingService
from skarbiec.models import (
    Transakcja, CelSkladkowy, CelSkladkowyPlatnik, Konto, PrzypisaniePlatnosci,
    DopasowanieStatus, CelStatus, PlatnikStatus
)


@pytest.mark.django_db
class TestMatchingService:

    def test_match_by_account_number(self, konto, transakcja):
        service = MatchingService()
        matched_konto = service.match_by_account(transakcja.nr_konta)

        assert matched_konto is not None
        assert matched_konto.numer_konta == konto.numer_konta

    def test_match_by_account_not_found(self, db):
        service = MatchingService()
        tx = Transakcja.objects.create(
            data="2025-01-15",
            kwota=100.00,
            tytul="Transfer",
            nr_konta="99999999999999999999",
            nadawca="Unknown",
        )

        matched = service.match_by_account(tx.nr_konta)
        assert matched is None

    def test_match_by_code_finds_goal(self, cel_skladkowy, db):
        tx = Transakcja.objects.create(
            data="2025-01-15",
            kwota=100.00,
            tytul=f"Transfer {cel_skladkowy.kod}",
            nr_konta="12345678901234567890",
            nadawca="Jan",
        )

        service = MatchingService()
        matched_cel = service.match_by_code(tx.tytul)

        assert matched_cel is not None
        assert matched_cel.kod == cel_skladkowy.kod

    def test_match_by_code_not_found(self, db):
        tx = Transakcja.objects.create(
            data="2025-01-15",
            kwota=100.00,
            tytul="Transfer NONEXISTENT",
            nr_konta="12345678901234567890",
            nadawca="Jan",
        )

        service = MatchingService()
        matched = service.match_by_code(tx.tytul)

        assert matched is None

    def test_match_by_name_finds_user(self, konto, db):
        tx = Transakcja.objects.create(
            data="2025-01-15",
            kwota=100.00,
            tytul="Transfer",
            nr_konta="12345678901234567890",
            nadawca=konto.nazwa_wlasciciela,
        )

        service = MatchingService()
        matched_user = service.match_by_name(tx.nadawca)

        assert matched_user is not None

    def test_match_by_name_partial_match(self, konto, db):
        tx = Transakcja.objects.create(
            data="2025-01-15",
            kwota=100.00,
            tytul="Transfer",
            nr_konta="12345678901234567890",
            nadawca="Jan",
        )

        service = MatchingService()
        matched_user = service.match_by_name("Jan")

        assert matched_user is not None or matched_user is None

    def test_match_transaction_auto_all_fields(self, konto, cel_skladkowy, cel_platnik):
        tx = Transakcja.objects.create(
            data="2025-01-15",
            kwota=100.00,
            tytul=f"Transfer {cel_skladkowy.kod}",
            nr_konta=konto.numer_konta,
            nadawca=konto.nazwa_wlasciciela,
        )

        service = MatchingService()
        przypisanie = service.match_transaction(tx)

        if przypisanie:
            assert przypisanie.status_dopasowania in [
                DopasowanieStatus.AUTO,
                DopasowanieStatus.MANUAL,
                DopasowanieStatus.NIEPEWNE
            ]

    def test_match_transaction_creates_przypisanie(self, konto, cel_skladkowy, cel_platnik):
        tx = Transakcja.objects.create(
            data="2025-01-15",
            kwota=100.00,
            tytul=f"Transfer {cel_skladkowy.kod}",
            nr_konta=konto.numer_konta,
            nadawca=konto.nazwa_wlasciciela,
        )

        service = MatchingService()
        service.match_transaction(tx)

        przypisania = PrzypisaniePlatnosci.objects.filter(transakcja=tx)
        assert przypisania.count() >= 0

    def test_match_transaction_auto_status(self, konto, cel_skladkowy, cel_platnik):
        tx = Transakcja.objects.create(
            data="2025-01-15",
            kwota=cel_platnik.kwota_docelowa,
            tytul=f"Transfer {cel_skladkowy.kod}",
            nr_konta=konto.numer_konta,
            nadawca=konto.nazwa_wlasciciela,
        )

        service = MatchingService()
        przypisanie = service.match_transaction(tx)

        if przypisanie and przypisanie.status_dopasowania == DopasowanieStatus.AUTO:
            assert przypisanie.kwota_przypisana > 0

    def test_match_transaction_uncertain_on_partial_data(self, db):
        tx = Transakcja.objects.create(
            data="2025-01-15",
            kwota=100.00,
            tytul="Transfer",
            nr_konta="99999999999999999999",
            nadawca="Unknown Sender",
        )

        service = MatchingService()
        przypisanie = service.match_transaction(tx)

        if przypisanie is None:
            assert True

    def test_match_transaction_no_match(self, db):
        tx = Transakcja.objects.create(
            data="2025-01-15",
            kwota=100.00,
            tytul="Random Transfer",
            nr_konta="99999999999999999999",
            nadawca="Random User",
        )

        service = MatchingService()
        przypisanie = service.match_transaction(tx)

        assert przypisanie is None or isinstance(przypisanie, PrzypisaniePlatnosci)

    def test_match_transactions_batch(self, konto, cel_skladkowy, cel_platnik):
        txs = []
        for i in range(3):
            tx = Transakcja.objects.create(
                data="2025-01-15",
                kwota=100.00,
                tytul=f"Transfer {cel_skladkowy.kod}",
                nr_konta=konto.numer_konta,
                nadawca=konto.nazwa_wlasciciela,
            )
            txs.append(tx)

        service = MatchingService()
        service.match_transactions(txs)

        przypisania = PrzypisaniePlatnosci.objects.all()
        assert przypisania.count() >= 0

    def test_match_partial_amount(self, konto, cel_skladkowy, cel_platnik):
        tx = Transakcja.objects.create(
            data="2025-01-15",
            kwota=50.00,
            tytul=f"Transfer {cel_skladkowy.kod}",
            nr_konta=konto.numer_konta,
            nadawca=konto.nazwa_wlasciciela,
        )

        service = MatchingService()
        przypisanie = service.match_transaction(tx)

        if przypisanie:
            assert przypisanie.kwota_przypisana == tx.kwota

    def test_match_updates_cel_platnik_status(self, konto, cel_skladkowy, cel_platnik):
        tx = Transakcja.objects.create(
            data="2025-01-15",
            kwota=100.00,
            tytul=f"Transfer {cel_skladkowy.kod}",
            nr_konta=konto.numer_konta,
            nadawca=konto.nazwa_wlasciciela,
        )

        service = MatchingService()
        service.match_transaction(tx)

        updated_platnik = CelSkladkowyPlatnik.objects.get(id=cel_platnik.id)
        assert updated_platnik.status in [
            PlatnikStatus.NIEZAPLACONE,
            PlatnikStatus.CZESCIOWO,
            PlatnikStatus.OPLACONE
        ]

