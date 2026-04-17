import pytest
from skarbiec.models import Order, OrderItem, Pin, Status
from skarbiec.services import PinCatalogService, OrderService, PricingEngine
from django.contrib.auth.models import User as DjangoUser


@pytest.mark.django_db
class TestPinOrderingWorkflow:

    def test_open_catalog_view_pins_workflow(self, db, user, multiple_pins):
        """Test: User opens catalog and sees available pins"""
        service = PinCatalogService()
        available = service.getAvailablePins()

        assert len(available) > 0
        assert all(p.active for p in available)

    def test_select_pin_add_to_cart_workflow(self, db, user, pin_available):
        """Test: User selects pin and adds to draft order"""
        order_service = OrderService()
        catalog_service = PinCatalogService()

        order = order_service.createDraftOrder(user)
        pin_details = catalog_service.getPinDetails([pin_available.id])

        order_service.addItemToOrder(order.id, pin_available.id, quantity=2)

        updated = Order.objects.get(id=order.id)
        assert updated.items.count() > 0

    def test_price_calculation_single_item_workflow(self, db, user, pin_available):
        """Test: Price calculated when item added"""
        order = Order.objects.create(
            created_by=user,
            status=Status.DRAFT,
            total_cost=0.00,
        )
        OrderItem.objects.create(
            order=order,
            pin=pin_available,
            quantity=5,
            unit_price=pin_available.price,
        )

        pricing = PricingEngine()
        items = [
            {"quantity": item.quantity, "unit_price": item.unit_price}
            for item in order.items.all()
        ]
        total = pricing.calculateTotal(items)

        expected = 5 * pin_available.price
        assert abs(total - expected) < 0.01

    def test_price_calculation_multiple_items_workflow(self, db, user, multiple_pins):
        """Test: Price calculated for multiple items"""
        order = Order.objects.create(
            created_by=user,
            status=Status.DRAFT,
            total_cost=0.00,
        )

        for i, pin in enumerate(multiple_pins[:3]):
            OrderItem.objects.create(
                order=order,
                pin=pin,
                quantity=i + 1,
                unit_price=pin.price,
            )

        pricing = PricingEngine()
        items = [
            {"quantity": item.quantity, "unit_price": item.unit_price}
            for item in order.items.all()
        ]
        total = pricing.calculateTotal(items)

        assert total > 0

    def test_complete_order_workflow_create_to_submit(self, db, user, pin_available, pin_expensive):
        """Test: Complete workflow from catalog to order submission"""
        order_service = OrderService()
        catalog_service = PinCatalogService()
        pricing_engine = PricingEngine()

        available_pins = catalog_service.getAvailablePins()
        assert pin_available in available_pins

        order = order_service.createDraftOrder(user)
        assert order.status == Status.DRAFT

        order_service.addItemToOrder(order.id, pin_available.id, quantity=3)
        order_service.addItemToOrder(order.id, pin_expensive.id, quantity=1)

        items_data = [
            {"quantity": item.quantity, "unit_price": item.unit_price}
            for item in order.items.all()
        ]
        total = pricing_engine.calculateTotal(items_data)

        order_service.submitOrder(order.id)

        final_order = Order.objects.get(id=order.id)
        assert final_order.status == Status.SUBMITTED
        assert final_order.total_cost > 0

    def test_multiple_items_same_pin_workflow(self, db, user, pin_available):
        """Test: Adding same pin multiple times increases quantity"""
        order_service = OrderService()

        order = order_service.createDraftOrder(user)

        order_service.addItemToOrder(order.id, pin_available.id, quantity=2)
        order_service.addItemToOrder(order.id, pin_available.id, quantity=3)

        updated_order = Order.objects.get(id=order.id)
        items = updated_order.items.filter(pin=pin_available)

        total_qty = sum(item.quantity for item in items)
        assert total_qty >= 5

    def test_modify_order_before_submission(self, db, user, multiple_pins):
        """Test: User modifies items before submitting"""
        order_service = OrderService()

        order = order_service.createDraftOrder(user)

        order_service.addItemToOrder(order.id, multiple_pins[0].id, quantity=5)
        item = order.items.first()

        order_service.updateItemQuantity(item.id, 10)

        updated_item = OrderItem.objects.get(id=item.id)
        assert updated_item.quantity == 10

    def test_remove_item_from_order_workflow(self, db, user, multiple_pins):
        """Test: User removes item from order"""
        order_service = OrderService()

        order = order_service.createDraftOrder(user)
        order_service.addItemToOrder(order.id, multiple_pins[0].id, quantity=5)

        order_service.removeItemFromOrder(order.id, multiple_pins[0].id)

        updated_order = Order.objects.get(id=order.id)
        assert updated_order.items.count() == 0

    def test_price_snapshot_locked_at_submission(self, db, user, pin_available):
        """Test: Prices locked when order submitted"""
        order = Order.objects.create(
            created_by=user,
            status=Status.DRAFT,
            total_cost=0.00,
        )

        original_price = pin_available.price
        OrderItem.objects.create(
            order=order,
            pin=pin_available,
            quantity=2,
            unit_price=original_price,
        )

        pin_available.price = 999.99
        pin_available.save()

        order_service = OrderService()
        order_service.submitOrder(order.id)

        item = order.items.first()
        assert item.unit_price == original_price
        assert item.unit_price != pin_available.price

    def test_sync_catalog_then_order_workflow(self, db, user, mocker):
        """Test: Sync catalog, then user can order"""
        mock_sync_data = [
            {"name": "Synced Pin", "description": "From external", "price": 20.0, "quantity": 100},
        ]
        mocker.patch.object(
            PinCatalogService,
            "_fetch_external_pins",
            return_value=mock_sync_data
        )

        catalog_service = PinCatalogService()
        catalog_service.syncPins()

        available = catalog_service.getAvailablePins()
        assert len(available) > 0

        pin = available[0]
        order_service = OrderService()
        order = order_service.createDraftOrder(user)
        order_service.addItemToOrder(order.id, pin.id, quantity=1)

        updated_order = Order.objects.get(id=order.id)
        assert updated_order.items.count() > 0

    def test_empty_catalog_workflow(self, db, user):
        """Test: No pins available shows empty message"""
        service = PinCatalogService()
        available = service.getAvailablePins()

        assert len(available) == 0

    def test_unavailable_pin_cannot_be_ordered(self, db, user, pin_unavailable):
        """Test: Cannot order pin marked as inactive"""
        order_service = OrderService()
        order = order_service.createDraftOrder(user)

        with pytest.raises(Exception):
            order_service.addItemToOrder(order.id, pin_unavailable.id, quantity=1)

    def test_insufficient_stock_workflow(self, db, user, pin_available):
        """Test: Cannot order more than available stock"""
        order_service = OrderService()
        order = order_service.createDraftOrder(user)

        with pytest.raises(Exception):
            order_service.addItemToOrder(order.id, pin_available.id, quantity=9999)

    def test_order_payment_workflow(self, db, user, pin_available):
        """Test: Submit order then mark as paid"""
        order_service = OrderService()

        order = order_service.createDraftOrder(user)
        order_service.addItemToOrder(order.id, pin_available.id, quantity=2)
        order_service.submitOrder(order.id)

        submitted_order = Order.objects.get(id=order.id)
        assert submitted_order.status == Status.SUBMITTED

        order_service.markOrderAsPaid(order.id)

        paid_order = Order.objects.get(id=order.id)
        assert paid_order.status == Status.PAID

    def test_user_order_history_workflow(self, db, user, multiple_pins):
        """Test: User can view all their orders"""
        order_service = OrderService()

        for i in range(3):
            order = order_service.createDraftOrder(user)
            order_service.addItemToOrder(order.id, multiple_pins[i].id, quantity=1)
            order_service.submitOrder(order.id)

        orders = order_service.getUserOrders(user.id)
        assert len(orders) == 3
        assert all(o.created_by == user for o in orders)

    def test_order_with_tax_calculation(self, db, user, multiple_pins):
        """Test: Pricing with tax applied"""
        order = Order.objects.create(
            created_by=user,
            status=Status.DRAFT,
            total_cost=0.00,
        )

        for pin in multiple_pins[:2]:
            OrderItem.objects.create(
                order=order,
                pin=pin,
                quantity=1,
                unit_price=pin.price,
            )

        pricing = PricingEngine()
        items = [
            {"quantity": item.quantity, "unit_price": item.unit_price}
            for item in order.items.all()
        ]

        subtotal = pricing.calculateTotal(items)
        total_with_tax = pricing.calculateTotal(items, tax_percent=23)

        assert total_with_tax > subtotal

    def test_bulk_order_discount_workflow(self, db, user, pin_available):
        """Test: Large order gets discount applied"""
        order = Order.objects.create(
            created_by=user,
            status=Status.DRAFT,
            total_cost=0.00,
        )

        OrderItem.objects.create(
            order=order,
            pin=pin_available,
            quantity=100,
            unit_price=pin_available.price,
        )

        pricing = PricingEngine()
        items = [
            {"quantity": item.quantity, "unit_price": item.unit_price}
            for item in order.items.all()
        ]

        regular_total = pricing.calculateTotal(items)
        discounted_total = pricing.calculateTotal(
            items,
            bulk_threshold=50,
            bulk_discount_percent=10
        )

        assert discounted_total < regular_total

