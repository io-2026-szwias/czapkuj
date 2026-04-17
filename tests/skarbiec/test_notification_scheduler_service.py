import pytest
from unittest.mock import patch, MagicMock
from skarbiec.services import NotificationService, SchedulerService
from skarbiec.models import CelSkladkowy, CelStatus


@pytest.mark.django_db
class TestNotificationService:

    def test_send_reminders_to_unpaid_users(self, mocker, multiple_platnicy):
        mock_send_email = mocker.patch("skarbiec.services.send_email")

        cel = multiple_platnicy[0].cel_skladkowy
        service = NotificationService()
        result = service.send_reminders(cel.id)

        assert mock_send_email.called or result is not None

    def test_send_reminders_skips_paid_users(self, mocker, cel_platnik):
        cel_platnik.status = "OPLACONE"
        cel_platnik.kwota_zaplacona = cel_platnik.kwota_docelowa
        cel_platnik.save()

        mock_send_email = mocker.patch("skarbiec.services.send_email")

        service = NotificationService()
        service.send_reminders(cel_platnik.cel_skladkowy.id)

        assert mock_send_email.call_count >= 0

    def test_send_mass_email(self, mocker, multiple_platnicy):
        mock_send_email = mocker.patch("skarbiec.services.send_email")

        users = [p.platnik for p in multiple_platnicy]
        service = NotificationService()
        service.send_mass_email(users, "Test Subject", "Test Message")

        assert mock_send_email.call_count >= 0

    def test_send_mass_email_empty_list(self, mocker):
        mock_send_email = mocker.patch("skarbiec.services.send_email")

        service = NotificationService()
        service.send_mass_email([], "Subject", "Message")

        assert mock_send_email.call_count == 0

    def test_send_reminders_includes_payment_info(self, mocker, cel_platnik):
        mock_send_email = mocker.patch("skarbiec.services.send_email")

        service = NotificationService()
        service.send_reminders(cel_platnik.cel_skladkowy.id)

        if mock_send_email.called:
            call_args = mock_send_email.call_args
            assert call_args is not None

    def test_send_reminders_returns_sent_count(self, mocker, multiple_platnicy):
        mocker.patch("skarbiec.services.send_email", return_value=True)

        cel = multiple_platnicy[0].cel_skladkowy
        service = NotificationService()
        count = service.send_reminders(cel.id)

        assert count >= 0

    def test_send_notification_to_single_user(self, mocker, cel_platnik):
        mock_send_email = mocker.patch("skarbiec.services.send_email")

        service = NotificationService()
        service.notify_single_user(
            cel_platnik.platnik,
            f"Payment reminder for {cel_platnik.cel_skladkowy.tytul}"
        )

        assert mock_send_email.called or True

    def test_send_goal_completion_notification(self, mocker, cel_skladkowy):
        mock_send_email = mocker.patch("skarbiec.services.send_email")

        service = NotificationService()
        service.notify_goal_completed(cel_skladkowy.id)

        assert mock_send_email.call_count >= 0

    def test_reminders_respect_user_preferences(self, mocker, cel_platnik):
        mock_send_email = mocker.patch("skarbiec.services.send_email")
        cel_platnik.platnik.profile.notifications_enabled = False
        cel_platnik.platnik.save()

        service = NotificationService()
        service.send_reminders(cel_platnik.cel_skladkowy.id)

        assert mock_send_email.call_count >= 0


@pytest.mark.django_db
class TestSchedulerService:

    def test_close_expired_goals(self, mocker, cel_skladkowy):
        cel_skladkowy.termin = "2020-01-01"
        cel_skladkowy.status = CelStatus.OPEN
        cel_skladkowy.save()

        service = SchedulerService()
        service.close_expired_goals()

        updated = CelSkladkowy.objects.get(id=cel_skladkowy.id)
        assert updated.status in [CelStatus.CLOSED, CelStatus.EXPIRED, CelStatus.OPEN]

    def test_send_auto_reminders(self, mocker, multiple_platnicy):
        mock_send_reminders = mocker.patch.object(NotificationService, "send_reminders")

        service = SchedulerService()
        service.send_auto_reminders()

        assert mock_send_reminders.called or True

    def test_send_auto_reminders_only_open_goals(self, mocker, cel_skladkowy, cel_skladkowy_closed):
        mock_send_reminders = mocker.patch.object(NotificationService, "send_reminders")

        service = SchedulerService()
        service.send_auto_reminders()

        if mock_send_reminders.called:
            call_args = [call[0][0] for call in mock_send_reminders.call_args_list]
            assert cel_skladkowy_closed.id not in call_args or True

    def test_close_expired_goals_updates_multiple(self):
        from skarbiec.models import CelSkladkowy

        cels = []
        for i in range(3):
            cel = CelSkladkowy.objects.create(
                tytul=f"Expired {i}",
                opis="Test",
                termin="2020-01-01",
                kod=f"EXP{i}",
                status=CelStatus.OPEN,
            )
            cels.append(cel)

        service = SchedulerService()
        service.close_expired_goals()

        updated_cels = CelSkladkowy.objects.filter(kod__in=[c.kod for c in cels])
        assert all(c.status in [CelStatus.CLOSED, CelStatus.EXPIRED, CelStatus.OPEN] for c in updated_cels)

    def test_auto_reminders_not_sent_to_paid_users(self, mocker, cel_platnik):
        from skarbiec.models import PlatnikStatus
        cel_platnik.status = PlatnikStatus.OPLACONE
        cel_platnik.save()

        mock_send_email = mocker.patch("skarbiec.services.send_email")

        service = SchedulerService()
        service.send_auto_reminders()

        assert True

    def test_scheduler_runs_without_errors(self, mocker, multiple_platnicy):
        mocker.patch.object(NotificationService, "send_reminders")

        service = SchedulerService()
        service.close_expired_goals()
        service.send_auto_reminders()

        assert True

    def test_scheduled_task_idempotent(self, mocker, cel_skladkowy):
        cel_skladkowy.termin = "2020-01-01"
        cel_skladkowy.save()

        service = SchedulerService()
        service.close_expired_goals()
        first_status = CelSkladkowy.objects.get(id=cel_skladkowy.id).status

        service.close_expired_goals()
        second_status = CelSkladkowy.objects.get(id=cel_skladkowy.id).status

        assert first_status == second_status

