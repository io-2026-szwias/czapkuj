import pytest
from skarbiec.services import OrderService, PricingEngine
from skarbiec.models import Order, OrderItem, Pin, Status


@pytest.mark.django_db
class TestOrderService:

    def test_create_draft_order(self, user):
        service = OrderService()
        order = service.createDraftOrder(user)

        assert order.id is not None
        assert order.created_by == user
        assert order.status == Status.DRAFT
        assert order.total_cost == 0.00

    def test_create_draft_order_with_items(self, user, pin_available):
        items = [{"pin_id": pin_available.id, "quantity": 5}]

        service = OrderService()
        order = service.createDraftOrder(user, items)

        assert order.id is not None
        assert order.items.count() >= 1

    def test_add_item_to_draft_order(self, order_draft, pin_available):
        service = OrderService()
        service.addItemToOrder(order_draft.id, pin_available.id, quantity=3)

        updated_order = Order.objects.get(id=order_draft.id)
        assert updated_order.items.count() >= 1

    def test_add_multiple_items_to_order(self, order_draft, multiple_pins):
        service = OrderService()

        for pin in multiple_pins[:3]:
            service.addItemToOrder(order_draft.id, pin.id, quantity=2)

        updated_order = Order.objects.get(id=order_draft.id)
        assert updated_order.items.count() == 3

    def test_remove_item_from_draft_order(self, order_draft, pin_available):
        OrderItem.objects.create(
            order=order_draft,
            pin=pin_available,
            quantity=5,
            unit_price=pin_available.price,
        )

        service = OrderService()
        service.removeItemFromOrder(order_draft.id, pin_available.id)

        updated_order = Order.objects.get(id=order_draft.id)
        assert updated_order.items.count() == 0

    def test_calculate_order_total(self, order_draft, multiple_pins):
        for i, pin in enumerate(multiple_pins[:3]):
            OrderItem.objects.create(
                order=order_draft,
                pin=pin,
                quantity=i + 1,
                unit_price=pin.price,
            )

        service = OrderService()
        total = service.calculateOrderTotal(order_draft.id)

        assert total > 0

    def test_calculate_order_total_empty_order(self, order_draft):
        service = OrderService()
        total = service.calculateOrderTotal(order_draft.id)

        assert total == 0.00

    def test_submit_order_changes_status(self, order_draft):
        service = OrderService()
        service.submitOrder(order_draft.id)

        updated = Order.objects.get(id=order_draft.id)
        assert updated.status == Status.SUBMITTED

    def test_submit_order_calculates_total(self, order_draft, pin_available):
        OrderItem.objects.create(
            order=order_draft,
            pin=pin_available,
            quantity=5,
            unit_price=pin_available.price,
        )

        service = OrderService()
        service.submitOrder(order_draft.id)

        updated = Order.objects.get(id=order_draft.id)
        assert updated.total_cost > 0

    def test_submit_order_locks_prices(self, order_draft, pin_available):
        original_price = pin_available.price
        OrderItem.objects.create(
            order=order_draft,
            pin=pin_available,
            quantity=2,
            unit_price=original_price,
        )

        pin_available.price = 999.99
        pin_available.save()

        service = OrderService()
        service.submitOrder(order_draft.id)

        item = order_draft.items.first()
        assert item.unit_price == original_price

    def test_mark_order_as_paid(self, order_submitted):
        service = OrderService()
        service.markOrderAsPaid(order_submitted.id)

        updated = Order.objects.get(id=order_submitted.id)
        assert updated.status == Status.PAID

    def test_get_order_details(self, order_draft, multiple_pins):
        for pin in multiple_pins[:2]:
            OrderItem.objects.create(
                order=order_draft,
                pin=pin,
                quantity=1,
                unit_price=pin.price,
            )

        service = OrderService()
        details = service.getOrderDetails(order_draft.id)

        assert details is not None
        assert details.id == order_draft.id

    def test_get_order_items(self, order_draft, multiple_pins):
        for i, pin in enumerate(multiple_pins[:3]):
            OrderItem.objects.create(
                order=order_draft,
                pin=pin,
                quantity=i + 1,
                unit_price=pin.price,
            )

        service = OrderService()
        items = service.getOrderItems(order_draft.id)

        assert len(items) == 3

    def test_update_item_quantity(self, order_draft, pin_available):
        item = OrderItem.objects.create(
            order=order_draft,
            pin=pin_available,
            quantity=5,
            unit_price=pin_available.price,
        )

        service = OrderService()
        service.updateItemQuantity(item.id, 10)

        updated_item = OrderItem.objects.get(id=item.id)
        assert updated_item.quantity == 10

    def test_cannot_submit_order_twice(self, order_submitted):
        service = OrderService()

        with pytest.raises(Exception):
            service.submitOrder(order_submitted.id)

    def test_cannot_add_to_submitted_order(self, order_submitted, pin_available):
        service = OrderService()

        with pytest.raises(Exception):
            service.addItemToOrder(order_submitted.id, pin_available.id, quantity=1)

    def test_order_with_unavailable_pin_fails(self, order_draft, pin_unavailable):
        service = OrderService()

        with pytest.raises(Exception):
            service.addItemToOrder(order_draft.id, pin_unavailable.id, quantity=1)

    def test_order_quantity_exceeds_stock_fails(self, order_draft, pin_available):
        service = OrderService()

        with pytest.raises(Exception):
            service.addItemToOrder(order_draft.id, pin_available.id, quantity=999)

    def test_get_user_orders(self, user):
        order1 = Order.objects.create(created_by=user, status=Status.DRAFT, total_cost=10.0)
        order2 = Order.objects.create(created_by=user, status=Status.SUBMITTED, total_cost=20.0)

        service = OrderService()
        orders = service.getUserOrders(user.id)

        assert len(orders) >= 2

    def test_get_user_draft_orders(self, user):
        Order.objects.create(created_by=user, status=Status.DRAFT, total_cost=10.0)
        Order.objects.create(created_by=user, status=Status.SUBMITTED, total_cost=20.0)

        service = OrderService()
        drafts = service.getUserOrders(user.id, status=Status.DRAFT)

        assert all(o.status == Status.DRAFT for o in drafts)

