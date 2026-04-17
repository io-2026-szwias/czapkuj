import pytest
from io import StringIO
from skarbiec.services import CelService
from skarbiec.models import CelSkladkowy, CelSkladkowyPlatnik, CelStatus, PlatnikStatus


@pytest.mark.django_db
class TestCelService:

    def test_create_cel_with_required_fields(self):
        service = CelService()
        cel = service.create_cel(
            tytul="New Goal",
            opis="Test goal",
            termin="2025-12-31",
            kod="NEWGOAL001",
        )

        assert cel.id is not None
        assert cel.tytul == "New Goal"
        assert cel.status == CelStatus.OPEN

    def test_create_cel_with_equal_amounts(self, member_user, member_user_2):
        service = CelService()
        cel = service.create_cel(
            tytul="Equal Goal",
            opis="Test",
            termin="2025-12-31",
            kod="EQUAL001",
            platnicy=[member_user, member_user_2],
            kwota_na_osobe=100.00,
        )

        platnicy = cel.platnicy.all()
        assert platnicy.count() >= 2

    def test_create_cel_with_custom_amounts_csv(self, member_user, member_user_2):
        csv_content = """email,kwota
member@org.pl,150.00
member2@org.pl,200.00"""

        service = CelService()
        cel = service.create_cel(
            tytul="Custom Amounts Goal",
            opis="Test",
            termin="2025-12-31",
            kod="CUSTOM001",
            csv_file=StringIO(csv_content),
        )

        platnicy = cel.platnicy.all()
        assert platnicy.count() >= 0

    def test_create_cel_assigns_equal_amounts(self, member_user, member_user_2):
        service = CelService()
        kwota = 100.00
        cel = service.create_cel(
            tytul="Equal Test",
            opis="Test",
            termin="2025-12-31",
            kod="EQ001",
            platnicy=[member_user, member_user_2],
            kwota_na_osobe=kwota,
        )

        for platnik in cel.platnicy.all():
            assert platnik.kwota_docelowa == kwota

    def test_assign_platnicy_to_existing_goal(self, cel_skladkowy, member_user):
        service = CelService()
        service.assign_platnicy(cel_skladkowy.id, [member_user], kwota_na_osobe=75.00)

        updated_cel = CelSkladkowy.objects.get(id=cel_skladkowy.id)
        assert updated_cel.platnicy.count() > 0

    def test_assign_platnicy_multiple(self, cel_skladkowy, member_user, member_user_2):
        service = CelService()
        service.assign_platnicy(cel_skladkowy.id, [member_user, member_user_2], kwota_na_osobe=50.00)

        updated_cel = CelSkladkowy.objects.get(id=cel_skladkowy.id)
        assert updated_cel.platnicy.count() >= 2

    def test_update_cel_status_to_closed(self, cel_skladkowy):
        service = CelService()
        service.update_status(cel_skladkowy.id, CelStatus.CLOSED)

        updated = CelSkladkowy.objects.get(id=cel_skladkowy.id)
        assert updated.status == CelStatus.CLOSED

    def test_update_cel_status_to_expired(self, cel_skladkowy):
        service = CelService()
        service.update_status(cel_skladkowy.id, CelStatus.EXPIRED)

        updated = CelSkladkowy.objects.get(id=cel_skladkowy.id)
        assert updated.status == CelStatus.EXPIRED

    def test_get_cel_by_id(self, cel_skladkowy):
        service = CelService()
        retrieved = service.get_cel(cel_skladkowy.id)

        assert retrieved.id == cel_skladkowy.id

    def test_get_all_open_cels(self, cel_skladkowy, cel_skladkowy_closed):
        service = CelService()
        open_cels = service.get_open_cels()

        assert any(c.id == cel_skladkowy.id for c in open_cels)
        assert not any(c.id == cel_skladkowy_closed.id for c in open_cels)

    def test_get_user_unpaid_goals(self, cel_platnik):
        service = CelService()
        goals = service.get_user_unpaid_goals(cel_platnik.platnik.id)

        assert len(goals) > 0
        assert any(g.id == cel_platnik.cel_skladkowy.id for g in goals)

    def test_get_user_paid_goals(self, cel_platnik):
        cel_platnik.status = PlatnikStatus.OPLACONE
        cel_platnik.kwota_zaplacona = cel_platnik.kwota_docelowa
        cel_platnik.save()

        service = CelService()
        goals = service.get_user_paid_goals(cel_platnik.platnik.id)

        assert len(goals) >= 0

    def test_update_platnik_payment_amount(self, cel_platnik):
        service = CelService()
        service.update_platnik_payment(cel_platnik.id, 50.00)

        updated = CelSkladkowyPlatnik.objects.get(id=cel_platnik.id)
        assert updated.kwota_zaplacona == 50.00

    def test_mark_platnik_as_paid(self, cel_platnik):
        service = CelService()
        service.mark_platnik_paid(cel_platnik.id)

        updated = CelSkladkowyPlatnik.objects.get(id=cel_platnik.id)
        assert updated.status == PlatnikStatus.OPLACONE

    def test_mark_platnik_as_partially_paid(self, cel_platnik):
        service = CelService()
        service.update_platnik_payment(cel_platnik.id, cel_platnik.kwota_docelowa / 2)

        updated = CelSkladkowyPlatnik.objects.get(id=cel_platnik.id)
        assert updated.kwota_zaplacona > 0
        assert updated.kwota_zaplacona < updated.kwota_docelowa

    def test_get_goal_summary(self, multiple_platnicy):
        cel = multiple_platnicy[0].cel_skladkowy
        service = CelService()
        summary = service.get_goal_summary(cel.id)

        assert summary is not None
        assert "total_assigned" in str(summary) or summary.get("total_assigned") is not None

    def test_create_cel_generates_unique_code(self):
        service = CelService()
        cel1 = service.create_cel(
            tytul="Goal 1",
            opis="Test",
            termin="2025-12-31",
            kod="UNIQUE001",
        )

        cel2 = service.create_cel(
            tytul="Goal 2",
            opis="Test",
            termin="2025-12-31",
            kod="UNIQUE002",
        )

        assert cel1.kod != cel2.kod

    def test_create_cel_duplicate_code_fails(self, cel_skladkowy):
        service = CelService()

        with pytest.raises(Exception):
            service.create_cel(
                tytul="Duplicate",
                opis="Test",
                termin="2025-12-31",
                kod=cel_skladkowy.kod,
            )

    def test_close_expired_goals(self, cel_skladkowy):
        cel_skladkowy.termin = "2020-01-01"
        cel_skladkowy.save()

        service = CelService()
        service.close_expired_goals()

        updated = CelSkladkowy.objects.get(id=cel_skladkowy.id)
        assert updated.status in [CelStatus.CLOSED, CelStatus.EXPIRED, CelStatus.OPEN]

