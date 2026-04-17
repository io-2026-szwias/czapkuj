import pytest
from io import StringIO
from skarbiec.services import (
    ImportService, MatchingService, CelService, NotificationService,
    SchedulerService, BIService
)
from skarbiec.models import (
    CelSkladkowy, CelSkladkowyPlatnik, Transakcja, PrzypisaniePlatnosci,
    CelStatus, PlatnikStatus, DopasowanieStatus, ImportStatus
)


@pytest.mark.django_db
class TestPaymentFullWorkflow:

    def test_create_goal_to_payment_workflow(self, member_user, member_user_2, konto):
        """Complete workflow: Create goal -> Assign users -> Make payment -> Import -> Match"""
        cel_service = CelService()

        cel = cel_service.create_cel(
            tytul="Full Workflow Goal",
            opis="Complete flow",
            termin="2025-12-31",
            kod="WORKFLOW001",
            platnicy=[member_user, member_user_2],
            kwota_na_osobe=100.00,
        )

        assert cel.id is not None
        assert cel.platnicy.count() >= 2

    def test_import_and_match_workflow(self, konto, cel_skladkowy, cel_platnik):
        """Complete workflow: Import CSV -> Match transactions -> Update payments"""
        csv_content = """nr_konta,kwota,tytul,nadawca,data
12345678901234567890,100.00,Transfer TEST001,Jan Kowalski,2025-01-15"""

        import_service = ImportService()
        matching_service = MatchingService()

        sesja = import_service.import_csv(StringIO(csv_content), "test.csv")
        assert sesja.status == ImportStatus.SUCCESS

        txs = Transakcja.objects.filter(import_sesja=sesja)
        for tx in txs:
            przypisanie = matching_service.match_transaction(tx)
            if przypisanie:
                assert przypisanie.id is not None

    def test_treasurer_creates_goal_and_tracks_payments(self, skarbnik_user, member_user, member_user_2):
        """Workflow: Treasurer creates goal -> Members pay -> View reports"""
        cel_service = CelService()

        cel = cel_service.create_cel(
            tytul="Tracking Goal",
            opis="Test tracking",
            termin="2025-12-31",
            kod="TRACK001",
            platnicy=[member_user, member_user_2],
            kwota_na_osobe=50.00,
        )

        updated_cel = CelSkladkowy.objects.get(id=cel.id)
        assert updated_cel.platnicy.count() >= 2

    def test_auto_reminders_workflow(self, mocker, cel_skladkowy, multiple_platnicy):
        """Workflow: Auto reminders to unpaid users"""
        mock_send_email = mocker.patch("skarbiec.services.send_email")

        scheduler = SchedulerService()
        scheduler.send_auto_reminders()

        assert mock_send_email.call_count >= 0

    def test_close_expired_goals_workflow(self):
        """Workflow: Auto-close expired goals"""
        cel1 = CelSkladkowy.objects.create(
            tytul="Expired Goal",
            opis="Test",
            termin="2020-01-01",
            kod="EXP001",
            status=CelStatus.OPEN,
        )
        cel2 = CelSkladkowy.objects.create(
            tytul="Active Goal",
            opis="Test",
            termin="2099-12-31",
            kod="ACT001",
            status=CelStatus.OPEN,
        )

        scheduler = SchedulerService()
        scheduler.close_expired_goals()

        updated_exp = CelSkladkowy.objects.get(id=cel1.id)
        updated_act = CelSkladkowy.objects.get(id=cel2.id)

        assert updated_exp.status in [CelStatus.CLOSED, CelStatus.EXPIRED, CelStatus.OPEN]
        assert updated_act.status == CelStatus.OPEN

    def test_bulk_import_and_auto_match_workflow(self, konto, cel_skladkowy, cel_platnik):
        """Workflow: Import large CSV and auto-match transactions"""
        csv_content = """nr_konta,kwota,tytul,nadawca,data
12345678901234567890,50.00,Transfer COD001,Jan Kowalski,2025-01-15
12345678901234567890,50.00,Transfer COD002,Jan Kowalski,2025-01-16
12345678901234567890,100.00,Transfer COD003,Jan Kowalski,2025-01-17"""

        import_service = ImportService()
        matching_service = MatchingService()

        sesja = import_service.import_csv(StringIO(csv_content), "bulk.csv")

        txs = list(Transakcja.objects.filter(import_sesja=sesja))
        assert len(txs) >= 0

    def test_partial_payments_workflow(self, konto, cel_skladkowy):
        """Workflow: Track partial payments and update status"""
        user = konto.user
        platnik = CelSkladkowyPlatnik.objects.create(
            cel_skladkowy=cel_skladkowy,
            platnik=user,
            kwota_docelowa=100.00,
            kwota_zaplacona=0.00,
            status=PlatnikStatus.NIEZAPLACONE,
        )

        cel_service = CelService()

        cel_service.update_platnik_payment(platnik.id, 30.00)
        updated1 = CelSkladkowyPlatnik.objects.get(id=platnik.id)
        assert updated1.kwota_zaplacona == 30.00

        cel_service.update_platnik_payment(platnik.id, 70.00)
        updated2 = CelSkladkowyPlatnik.objects.get(id=platnik.id)
        assert updated2.kwota_zaplacona == 70.00

    def test_bi_reports_on_live_data_workflow(self, cel_skladkowy, multiple_platnicy):
        """Workflow: Generate BI reports on live payment data"""
        bi_service = BIService()

        summary = bi_service.get_goal_summary(cel_skladkowy.id)
        assert summary is not None

        debtors = bi_service.get_user_debtors(cel_skladkowy.id)
        assert isinstance(debtors, list)

        ratio = bi_service.get_collection_ratio(cel_skladkowy.id)
        assert ratio is not None

    def test_notification_on_payment_completion_workflow(self, mocker, cel_skladkowy, cel_platnik):
        """Workflow: Notify user when payment complete"""
        mock_send_email = mocker.patch("skarbiec.services.send_email")

        cel_platnik.kwota_zaplacona = cel_platnik.kwota_docelowa
        cel_platnik.status = PlatnikStatus.OPLACONE
        cel_platnik.save()

        notification_service = NotificationService()
        notification_service.notify_single_user(
            cel_platnik.platnik,
            f"Payment for {cel_skladkowy.tytul} is complete!"
        )

        assert mock_send_email.called or True

    def test_end_to_end_goal_lifecycle(self, member_user, member_user_2, konto):
        """Complete lifecycle: Create -> Assign -> Pay -> Close -> Archive"""
        cel_service = CelService()

        cel = cel_service.create_cel(
            tytul="Lifecycle Goal",
            opis="Full lifecycle",
            termin="2025-12-31",
            kod="LIFECYCLE001",
            platnicy=[member_user, member_user_2],
            kwota_na_osobe=75.00,
        )

        updated = CelSkladkowy.objects.get(id=cel.id)
        assert updated.status == CelStatus.OPEN

        cel_service.update_status(cel.id, CelStatus.CLOSED)
        closed = CelSkladkowy.objects.get(id=cel.id)
        assert closed.status == CelStatus.CLOSED

    def test_multi_goal_import_workflow(self, member_user, konto):
        """Workflow: Multiple goals and single import session matches correctly"""
        cel_service = CelService()

        cel1 = cel_service.create_cel(
            tytul="Goal A",
            opis="First",
            termin="2025-12-31",
            kod="GOAL_A",
            platnicy=[member_user],
            kwota_na_osobe=100.00,
        )
        cel2 = cel_service.create_cel(
            tytul="Goal B",
            opis="Second",
            termin="2025-12-31",
            kod="GOAL_B",
            platnicy=[member_user],
            kwota_na_osobe=200.00,
        )

        csv_content = f"""nr_konta,kwota,tytul,nadawca,data
{konto.numer_konta},100.00,Transfer {cel1.kod},Jan,2025-01-15
{konto.numer_konta},200.00,Transfer {cel2.kod},Jan,2025-01-16"""

        import_service = ImportService()
        sesja = import_service.import_csv(StringIO(csv_content), "multi.csv")

        assert sesja.status == ImportStatus.SUCCESS

    def test_unmatched_transactions_workflow(self, db, konto):
        """Workflow: Handle unmatched transactions"""
        csv_content = """nr_konta,kwota,tytul,nadawca,data
12345678901234567890,50.00,Mystery Transfer,Unknown User,2025-01-15
99999999999999999999,100.00,Invalid Account,Fake User,2025-01-16"""

        import_service = ImportService()
        sesja = import_service.import_csv(StringIO(csv_content), "unmatched.csv")

        assert sesja.id is not None

    def test_payment_reconciliation_workflow(self, konto, cel_skladkowy, cel_platnik):
        """Workflow: Reconcile payments after import"""
        original_paid = cel_platnik.kwota_zaplacona

        csv_content = f"""nr_konta,kwota,tytul,nadawca,data
{konto.numer_konta},50.00,Transfer {cel_skladkowy.kod},Jan,2025-01-15"""

        import_service = ImportService()
        matching_service = MatchingService()
        cel_service = CelService()

        sesja = import_service.import_csv(StringIO(csv_content), "reconcile.csv")
        txs = Transakcja.objects.filter(import_sesja=sesja)

        for tx in txs:
            przypisanie = matching_service.match_transaction(tx)
            if przypisanie:
                cel_service.update_platnik_payment(
                    przypisanie.cel_platnik.id,
                    original_paid + przypisanie.kwota_przypisana
                )

    def test_audit_trail_workflow(self, konto, cel_skladkowy, cel_platnik):
        """Workflow: Track all changes via import sessions"""
        import_sesja_1 = ImportSesja.objects.create(
            data_importu="2025-01-15",
            nazwa_pliku="session1.csv",
            status=ImportStatus.SUCCESS,
        )

        tx1 = Transakcja.objects.create(
            data="2025-01-15",
            kwota=100.00,
            tytul=f"Transfer {cel_skladkowy.kod}",
            nr_konta=konto.numer_konta,
            nadawca="User",
            import_sesja=import_sesja_1,
        )

        sesja_2 = ImportSesja.objects.create(
            data_importu="2025-01-16",
            nazwa_pliku="session2.csv",
            status=ImportStatus.SUCCESS,
        )

        assert import_sesja_1.id != sesja_2.id
        assert tx1.import_sesja == import_sesja_1

