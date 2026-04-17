import pytest
from skarbiec.models import Pin, Order, OrderItem, Status


@pytest.mark.django_db
class TestPinModel:

    def test_pin_create_with_required_fields(self):
        pin = Pin.objects.create(
            name="Test Pin",
            description="Test description",
            price=10.99,
            available_quantity=50,
            active=True,
        )
        assert pin.id is not None
        assert pin.name == "Test Pin"
        assert pin.price == 10.99
        assert pin.available_quantity == 50
        assert pin.active is True

    def test_pin_default_active_false(self):
        pin = Pin.objects.create(
            name="Inactive Pin",
            description="Test",
            price=5.00,
            available_quantity=10,
        )
        assert pin.active is False

    def test_pin_available_quantity_can_be_zero(self):
        pin = Pin.objects.create(
            name="Out of Stock",
            description="Test",
            price=10.00,
            available_quantity=0,
            active=True,
        )
        assert pin.available_quantity == 0

    def test_pin_price_decimal_precision(self):
        pin = Pin.objects.create(
            name="Precise Pin",
            description="Test",
            price=99.99,
            available_quantity=1,
            active=True,
        )
        assert pin.price == 99.99

    def test_pin_name_required(self, db):
        with pytest.raises(Exception):
            Pin.objects.create(
                description="No name",
                price=10.00,
                available_quantity=5,
            )

    def test_pin_price_required(self, db):
        with pytest.raises(Exception):
            Pin.objects.create(
                name="No Price Pin",
                description="Test",
                available_quantity=5,
            )

    def test_pin_is_available_when_active_and_stock(self):
        pin = Pin.objects.create(
            name="Available",
            description="Test",
            price=10.00,
            available_quantity=10,
            active=True,
        )
        assert pin.active is True
        assert pin.available_quantity > 0

    def test_pin_is_unavailable_when_inactive(self):
        pin = Pin.objects.create(
            name="Inactive",
            description="Test",
            price=10.00,
            available_quantity=10,
            active=False,
        )
        assert pin.active is False

    def test_pin_is_unavailable_when_no_stock(self):
        pin = Pin.objects.create(
            name="Out of Stock",
            description="Test",
            price=10.00,
            available_quantity=0,
            active=True,
        )
        assert pin.available_quantity == 0

    def test_multiple_pins_same_price(self, db):
        Pin.objects.create(
            name="Pin A",
            description="A",
            price=10.00,
            available_quantity=5,
            active=True,
        )
        Pin.objects.create(
            name="Pin B",
            description="B",
            price=10.00,
            available_quantity=5,
            active=True,
        )
        assert Pin.objects.filter(price=10.00).count() == 2

    def test_pin_update_stock_quantity(self, pin_available):
        pin_available.available_quantity = 25
        pin_available.save()

        updated = Pin.objects.get(id=pin_available.id)
        assert updated.available_quantity == 25


@pytest.mark.django_db
class TestOrderModel:

    def test_order_create_with_required_fields(self, user):
        order = Order.objects.create(
            created_by=user,
            status=Status.DRAFT,
            total_cost=0.00,
        )
        assert order.id is not None
        assert order.created_by == user
        assert order.status == Status.DRAFT
        assert order.total_cost == 0.00

    def test_order_default_status_draft(self, user):
        order = Order.objects.create(
            created_by=user,
            total_cost=0.00,
        )
        assert order.status == Status.DRAFT

    def test_order_created_at_is_set_automatically(self, user):
        order = Order.objects.create(
            created_by=user,
            status=Status.DRAFT,
            total_cost=0.00,
        )
        assert order.created_at is not None

    def test_order_total_cost_zero_initially(self, user):
        order = Order.objects.create(
            created_by=user,
            status=Status.DRAFT,
        )
        assert order.total_cost == 0.00

    def test_order_status_transitions(self, order_draft):
        order_draft.status = Status.SUBMITTED
        order_draft.save()
        assert order_draft.status == Status.SUBMITTED

        order_draft.status = Status.PAID
        order_draft.save()
        assert order_draft.status == Status.PAID

    def test_order_update_total_cost(self, order_draft):
        order_draft.total_cost = 99.99
        order_draft.save()

        updated = Order.objects.get(id=order_draft.id)
        assert updated.total_cost == 99.99

    def test_order_has_items(self, order_draft, pin_available):
        item = OrderItem.objects.create(
            order=order_draft,
            pin=pin_available,
            quantity=5,
            unit_price=10.99,
        )

        items = order_draft.items.all()
        assert items.count() == 1
        assert item in items

    def test_user_can_have_multiple_orders(self, user):
        order1 = Order.objects.create(
            created_by=user,
            status=Status.DRAFT,
            total_cost=10.00,
        )
        order2 = Order.objects.create(
            created_by=user,
            status=Status.SUBMITTED,
            total_cost=20.00,
        )

        user_orders = Order.objects.filter(created_by=user)
        assert user_orders.count() == 2

    def test_order_filter_by_status(self, user):
        Order.objects.create(created_by=user, status=Status.DRAFT, total_cost=10.00)
        Order.objects.create(created_by=user, status=Status.DRAFT, total_cost=20.00)
        Order.objects.create(created_by=user, status=Status.SUBMITTED, total_cost=30.00)

        draft_orders = Order.objects.filter(status=Status.DRAFT)
        assert draft_orders.count() == 2


@pytest.mark.django_db
class TestOrderItemModel:

    def test_order_item_create_with_required_fields(self, order_draft, pin_available):
        item = OrderItem.objects.create(
            order=order_draft,
            pin=pin_available,
            quantity=5,
            unit_price=10.99,
        )
        assert item.id is not None
        assert item.order == order_draft
        assert item.pin == pin_available
        assert item.quantity == 5
        assert item.unit_price == 10.99

    def test_order_item_quantity_must_be_positive(self, db, order_draft, pin_available):
        with pytest.raises(Exception):
            OrderItem.objects.create(
                order=order_draft,
                pin=pin_available,
                quantity=0,
                unit_price=10.00,
            )

    def test_order_item_unit_price_can_differ_from_pin_price(self, order_draft, pin_available):
        item = OrderItem.objects.create(
            order=order_draft,
            pin=pin_available,
            quantity=2,
            unit_price=8.50,
        )
        assert item.unit_price != pin_available.price
        assert item.unit_price == 8.50

    def test_order_item_unit_price_captures_snapshot(self, order_draft, pin_available):
        original_price = pin_available.price
        item = OrderItem.objects.create(
            order=order_draft,
            pin=pin_available,
            quantity=3,
            unit_price=original_price,
        )

        pin_available.price = 99.99
        pin_available.save()

        item_refreshed = OrderItem.objects.get(id=item.id)
        assert item_refreshed.unit_price == original_price

    def test_order_can_have_multiple_items(self, order_draft, multiple_pins):
        for i, pin in enumerate(multiple_pins[:3]):
            OrderItem.objects.create(
                order=order_draft,
                pin=pin,
                quantity=i + 1,
                unit_price=pin.price,
            )

        items = order_draft.items.all()
        assert items.count() == 3

    def test_order_item_links_order_and_pin(self, order_draft, pin_available):
        item = OrderItem.objects.create(
            order=order_draft,
            pin=pin_available,
            quantity=1,
            unit_price=pin_available.price,
        )

        assert item.order.id == order_draft.id
        assert item.pin.id == pin_available.id

    def test_same_pin_multiple_items_in_order(self, order_draft, pin_available):
        OrderItem.objects.create(
            order=order_draft,
            pin=pin_available,
            quantity=5,
            unit_price=pin_available.price,
        )
        OrderItem.objects.create(
            order=order_draft,
            pin=pin_available,
            quantity=3,
            unit_price=pin_available.price,
        )

        items = order_draft.items.filter(pin=pin_available)
        assert items.count() == 2
        total_qty = sum(item.quantity for item in items)
        assert total_qty == 8

