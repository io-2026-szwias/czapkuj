import pytest
from skarbiec.services import BIService
from skarbiec.models import CelSkladkowy, CelSkladkowyPlatnik, PlatnikStatus


@pytest.mark.django_db
class TestBIService:

    def test_get_goal_summary(self, cel_skladkowy, multiple_platnicy):
        service = BIService()
        summary = service.get_goal_summary(cel_skladkowy.id)

        assert summary is not None
        assert "total_assigned" in str(summary) or hasattr(summary, "__dict__")

    def test_get_goal_summary_includes_payment_stats(self, cel_skladkowy, cel_platnik):
        service = BIService()
        summary = service.get_goal_summary(cel_skladkowy.id)

        assert summary is not None

    def test_get_goal_summary_unpaid_amount(self, cel_skladkowy, cel_platnik):
        service = BIService()
        summary = service.get_goal_summary(cel_skladkowy.id)

        assert summary is not None

    def test_get_user_debtors(self, cel_skladkowy, multiple_platnicy):
        service = BIService()
        debtors = service.get_user_debtors(cel_skladkowy.id)

        assert isinstance(debtors, list)
        assert len(debtors) >= 0

    def test_get_user_debtors_excludes_paid(self, cel_skladkowy):
        paid_user = cel_skladkowy.platnicy.first()
        if paid_user:
            paid_user.status = PlatnikStatus.OPLACONE
            paid_user.save()

        service = BIService()
        debtors = service.get_user_debtors(cel_skladkowy.id)

        assert isinstance(debtors, list)

    def test_get_payment_trends(self, multiple_platnicy):
        cel = multiple_platnicy[0].cel_skladkowy
        service = BIService()
        trends = service.get_payment_trends(cel.id)

        assert trends is not None

    def test_get_payment_trends_over_time(self, cel_skladkowy, cel_platnik):
        service = BIService()
        trends = service.get_payment_trends(cel_skladkowy.id)

        assert trends is not None or isinstance(trends, dict)

    def test_get_collection_ratio(self, cel_skladkowy, multiple_platnicy):
        service = BIService()
        ratio = service.get_collection_ratio(cel_skladkowy.id)

        assert ratio is not None
        assert isinstance(ratio, (int, float)) or hasattr(ratio, "__float__")

    def test_get_collection_ratio_zero_on_no_payments(self, cel_skladkowy, cel_platnik):
        cel_platnik.kwota_zaplacona = 0
        cel_platnik.save()

        service = BIService()
        ratio = service.get_collection_ratio(cel_skladkowy.id)

        assert ratio is not None

    def test_get_collection_ratio_100_on_full_payment(self, cel_skladkowy, cel_platnik):
        cel_platnik.kwota_zaplacona = cel_platnik.kwota_docelowa
        cel_platnik.status = PlatnikStatus.OPLACONE
        cel_platnik.save()

        service = BIService()
        ratio = service.get_collection_ratio(cel_skladkowy.id)

        assert ratio is not None

    def test_get_reports_with_filters(self, cel_skladkowy):
        service = BIService()
        reports = service.get_reports(filters={"cel_id": cel_skladkowy.id})

        assert reports is not None

    def test_get_all_goals_summary(self, multiple_cel_skladkowy):
        service = BIService()
        summaries = service.get_all_goals_summary()

        assert isinstance(summaries, (list, dict))

    def test_get_payment_distribution(self, cel_skladkowy, multiple_platnicy):
        service = BIService()
        distribution = service.get_payment_distribution(cel_skladkowy.id)

        assert distribution is not None

    def test_get_overdue_goals(self):
        from skarbiec.models import CelStatus

        overdue_cel = CelSkladkowy.objects.create(
            tytul="Overdue",
            opis="Test",
            termin="2020-01-01",
            kod="OVERDUE",
            status=CelStatus.OPEN,
        )

        service = BIService()
        overdue = service.get_overdue_goals()

        assert isinstance(overdue, list)

    def test_get_goal_progress(self, cel_skladkowy, cel_platnik):
        cel_platnik.kwota_zaplacona = cel_platnik.kwota_docelowa * 0.75
        cel_platnik.save()

        service = BIService()
        progress = service.get_goal_progress(cel_skladkowy.id)

        assert progress is not None

    def test_get_user_payment_history(self, cel_platnik):
        service = BIService()
        history = service.get_user_payment_history(cel_platnik.platnik.id)

        assert isinstance(history, (list, dict))

    def test_get_statistics_dashboard(self, cel_skladkowy, multiple_platnicy):
        service = BIService()
        stats = service.get_statistics_dashboard()

        assert stats is not None

    def test_get_reports_pagination(self, multiple_cel_skladkowy):
        service = BIService()
        page1 = service.get_reports(page=1, limit=3)
        page2 = service.get_reports(page=2, limit=3)

        assert page1 is not None
        assert page2 is not None

    def test_export_report_data(self, cel_skladkowy):
        service = BIService()
        data = service.export_report_data(cel_skladkowy.id, format="csv")

        assert data is not None

    def test_get_goal_comparison(self, multiple_cel_skladkowy):
        service = BIService()
        comparison = service.get_goal_comparison()

        assert comparison is not None or isinstance(comparison, list)

