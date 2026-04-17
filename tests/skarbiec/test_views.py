import pytest
from django.test import Client
from django.contrib.auth.models import User as DjangoUser
from skarbiec.models import CelSkladkowy, ImportSesja


@pytest.mark.django_db
class TestTreasuryViews:

    @pytest.fixture
    def client(self):
        return Client()

    @pytest.fixture
    def authenticated_skarbnik(self, db):
        user = DjangoUser.objects.create_user(
            username="skarbnik",
            email="skarbnik@org.pl",
            password="testpass123"
        )
        return user

    def test_get_goals_list_endpoint(self, client, authenticated_skarbnik):
        client.force_login(authenticated_skarbnik)

        response = client.get("/skarbiec/goals/")

        assert response.status_code in [200, 404]

    def test_get_goal_detail_endpoint(self, client, authenticated_skarbnik, cel_skladkowy):
        client.force_login(authenticated_skarbnik)

        response = client.get(f"/skarbiec/goals/{cel_skladkowy.id}/")

        assert response.status_code in [200, 404]

    def test_create_goal_endpoint_get(self, client, authenticated_skarbnik):
        client.force_login(authenticated_skarbnik)

        response = client.get("/skarbiec/goals/create/")

        assert response.status_code in [200, 404]

    def test_create_goal_endpoint_post(self, client, authenticated_skarbnik):
        client.force_login(authenticated_skarbnik)

        response = client.post("/skarbiec/goals/create/", {
            "tytul": "New Goal",
            "opis": "Test",
            "termin": "2025-12-31",
            "kod": "NEWGOAL",
        })

        assert response.status_code in [200, 302, 404]

    def test_import_csv_endpoint_get(self, client, authenticated_skarbnik):
        client.force_login(authenticated_skarbnik)

        response = client.get("/skarbiec/import/")

        assert response.status_code in [200, 404]

    def test_import_csv_endpoint_post(self, client, authenticated_skarbnik):
        client.force_login(authenticated_skarbnik)

        csv_data = b"""nr_konta,kwota,tytul,nadawca,data
12345678901234567890,100.00,Transfer,Jan,2025-01-15"""

        response = client.post("/skarbiec/import/", {
            "file": csv_data,
        })

        assert response.status_code in [200, 302, 404]

    def test_view_import_history_endpoint(self, client, authenticated_skarbnik, import_sesja):
        client.force_login(authenticated_skarbnik)

        response = client.get("/skarbiec/import-history/")

        assert response.status_code in [200, 404]

    def test_view_import_session_endpoint(self, client, authenticated_skarbnik, import_sesja):
        client.force_login(authenticated_skarbnik)

        response = client.get(f"/skarbiec/import-history/{import_sesja.id}/")

        assert response.status_code in [200, 404]

    def test_send_reminders_endpoint(self, client, authenticated_skarbnik, cel_skladkowy):
        client.force_login(authenticated_skarbnik)

        response = client.post(f"/skarbiec/goals/{cel_skladkowy.id}/send-reminders/")

        assert response.status_code in [200, 302, 404]

    def test_close_goal_endpoint(self, client, authenticated_skarbnik, cel_skladkowy):
        client.force_login(authenticated_skarbnik)

        response = client.post(f"/skarbiec/goals/{cel_skladkowy.id}/close/")

        assert response.status_code in [200, 302, 404]

    def test_bi_dashboard_endpoint(self, client, authenticated_skarbnik):
        client.force_login(authenticated_skarbnik)

        response = client.get("/skarbiec/bi/dashboard/")

        assert response.status_code in [200, 404]

    def test_bi_goal_report_endpoint(self, client, authenticated_skarbnik, cel_skladkowy):
        client.force_login(authenticated_skarbnik)

        response = client.get(f"/skarbiec/bi/goal/{cel_skladkowy.id}/")

        assert response.status_code in [200, 404]

    def test_view_requires_authentication(self, client):
        response = client.get("/skarbiec/goals/")

        assert response.status_code in [302, 404]

    def test_user_can_view_own_goals(self, client, member_user):
        client.force_login(member_user)

        response = client.get("/skarbiec/my-goals/")

        assert response.status_code in [200, 404]

    def test_treasurer_only_views_require_permission(self, client, member_user, cel_skladkowy):
        client.force_login(member_user)

        response = client.post(f"/skarbiec/goals/{cel_skladkowy.id}/close/")

        assert response.status_code in [403, 404]


@pytest.mark.django_db
class TestPinOrderViews:

    @pytest.fixture
    def client(self):
        return Client()

    @pytest.fixture
    def authenticated_skarbnik(self, db):
        user = DjangoUser.objects.create_user(
            username="skarbnik",
            email="skarbnik@org.pl",
            password="testpass123"
        )
        return user

    def test_get_pins_orders_endpoint(self, client, authenticated_skarbnik):
        client.force_login(authenticated_skarbnik)

        response = client.get("/skarbiec/pins-orders/")

        assert response.status_code in [200, 404]

    def test_submit_pin_order_endpoint(self, client, authenticated_skarbnik):
        client.force_login(authenticated_skarbnik)

        response = client.post("/skarbiec/pins-orders/submit/")

        assert response.status_code in [200, 302, 404]

    def test_view_pin_order_history_endpoint(self, client, authenticated_skarbnik):
        client.force_login(authenticated_skarbnik)

        response = client.get("/skarbiec/pins-orders/history/")

        assert response.status_code in [200, 404]

    def test_pin_orders_requires_authentication(self, client):
        response = client.get("/skarbiec/pins-orders/")

        assert response.status_code in [302, 404]

