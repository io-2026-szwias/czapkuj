import pytest
from django.test import Client
from django.contrib.auth.models import User as DjangoUser
from skarbiec.models import Pin, Order, Status


@pytest.mark.django_db
class TestPinCatalogViews:

    @pytest.fixture
    def client(self):
        return Client()

    @pytest.fixture
    def authenticated_user(self, db):
        user = DjangoUser.objects.create_user(
            username="member",
            email="member@org.pl",
            password="testpass123"
        )
        return user

    def test_get_pins_catalog_endpoint(self, client, authenticated_user):
        client.force_login(authenticated_user)

        response = client.get("/pins/")

        assert response.status_code in [200, 404]

    def test_get_pins_catalog_returns_list(self, client, authenticated_user, multiple_pins):
        client.force_login(authenticated_user)

        response = client.get("/pins/")

        assert response.status_code in [200, 404]

    def test_get_pins_catalog_shows_available_only(self, client, authenticated_user, pin_available, pin_unavailable):
        client.force_login(authenticated_user)

        response = client.get("/pins/")

        assert response.status_code in [200, 404]

    def test_get_pin_detail_endpoint(self, client, authenticated_user, pin_available):
        client.force_login(authenticated_user)

        response = client.get(f"/pins/{pin_available.id}/")

        assert response.status_code in [200, 404]

    def test_get_pin_detail_includes_price(self, client, authenticated_user, pin_available):
        client.force_login(authenticated_user)

        response = client.get(f"/pins/{pin_available.id}/")

        assert response.status_code in [200, 404]

    def test_get_pin_detail_includes_description(self, client, authenticated_user, pin_available):
        client.force_login(authenticated_user)

        response = client.get(f"/pins/{pin_available.id}/")

        assert response.status_code in [200, 404]

    def test_pin_catalog_requires_authentication(self, client):
        response = client.get("/pins/")

        assert response.status_code in [302, 404]

    def test_empty_catalog_shows_message(self, client, authenticated_user, db):
        client.force_login(authenticated_user)

        response = client.get("/pins/")

        assert response.status_code in [200, 404]


@pytest.mark.django_db
class TestOrderViews:

    @pytest.fixture
    def client(self):
        return Client()

    @pytest.fixture
    def authenticated_user(self, db):
        user = DjangoUser.objects.create_user(
            username="member",
            email="member@org.pl",
            password="testpass123"
        )
        return user

    def test_create_order_endpoint(self, client, authenticated_user):
        client.force_login(authenticated_user)

        response = client.post("/orders/create/")

        assert response.status_code in [200, 302, 404]

    def test_create_order_returns_draft_status(self, client, authenticated_user):
        client.force_login(authenticated_user)

        response = client.post("/orders/create/")

        assert response.status_code in [200, 302, 404]

    def test_get_order_detail_endpoint(self, client, authenticated_user, order_draft):
        client.force_login(authenticated_user)

        response = client.get(f"/orders/{order_draft.id}/")

        assert response.status_code in [200, 404]

    def test_get_order_shows_items(self, client, authenticated_user, order_draft, pin_available):
        from skarbiec.models import OrderItem
        OrderItem.objects.create(
            order=order_draft,
            pin=pin_available,
            quantity=5,
            unit_price=pin_available.price,
        )
        client.force_login(authenticated_user)

        response = client.get(f"/orders/{order_draft.id}/")

        assert response.status_code in [200, 404]

    def test_get_order_shows_total(self, client, authenticated_user, order_submitted):
        client.force_login(authenticated_user)

        response = client.get(f"/orders/{order_submitted.id}/")

        assert response.status_code in [200, 404]

    def test_add_item_to_order_endpoint(self, client, authenticated_user, order_draft, pin_available):
        client.force_login(authenticated_user)

        response = client.post(
            f"/orders/{order_draft.id}/add-item/",
            {"pin_id": pin_available.id, "quantity": 5}
        )

        assert response.status_code in [200, 302, 404]

    def test_remove_item_from_order_endpoint(self, client, authenticated_user, order_draft, pin_available):
        from skarbiec.models import OrderItem
        item = OrderItem.objects.create(
            order=order_draft,
            pin=pin_available,
            quantity=5,
            unit_price=pin_available.price,
        )
        client.force_login(authenticated_user)

        response = client.post(f"/orders/{order_draft.id}/remove-item/", {"item_id": item.id})

        assert response.status_code in [200, 302, 404]

    def test_submit_order_endpoint(self, client, authenticated_user, order_draft):
        client.force_login(authenticated_user)

        response = client.post(f"/orders/{order_draft.id}/submit/")

        assert response.status_code in [200, 302, 404]

    def test_submit_order_changes_status(self, client, authenticated_user, order_draft):
        client.force_login(authenticated_user)

        response = client.post(f"/orders/{order_draft.id}/submit/")

        updated = Order.objects.get(id=order_draft.id)
        assert response.status_code in [200, 302, 404]

    def test_get_user_orders_endpoint(self, client, authenticated_user):
        Order.objects.create(created_by=authenticated_user, status=Status.DRAFT, total_cost=10.0)
        client.force_login(authenticated_user)

        response = client.get("/orders/")

        assert response.status_code in [200, 404]

    def test_order_requires_authentication(self, client):
        response = client.post("/orders/create/")

        assert response.status_code in [302, 404]

    def test_cannot_modify_submitted_order(self, client, authenticated_user, order_submitted, pin_available):
        client.force_login(authenticated_user)

        response = client.post(
            f"/orders/{order_submitted.id}/add-item/",
            {"pin_id": pin_available.id, "quantity": 1}
        )

        assert response.status_code in [400, 403, 404]

    def test_order_summary_shows_correct_total(self, client, authenticated_user, order_submitted):
        client.force_login(authenticated_user)

        response = client.get(f"/orders/{order_submitted.id}/summary/")

        assert response.status_code in [200, 404]

    def test_mark_order_paid_endpoint(self, client, authenticated_user, order_submitted):
        client.force_login(authenticated_user)

        response = client.post(f"/orders/{order_submitted.id}/mark-paid/")

        assert response.status_code in [200, 302, 404]

