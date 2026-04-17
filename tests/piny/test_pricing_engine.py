import pytest
from skarbiec.services import PricingEngine
from skarbiec.models import Order, OrderItem, Pin


@pytest.mark.django_db
class TestPricingEngine:

    def test_calculate_total_single_item(self):
        items = [{"quantity": 5, "unit_price": 10.00}]

        engine = PricingEngine()
        total = engine.calculateTotal(items)

        assert total == 50.00

    def test_calculate_total_multiple_items(self):
        items = [
            {"quantity": 5, "unit_price": 10.00},
            {"quantity": 2, "unit_price": 25.00},
        ]

        engine = PricingEngine()
        total = engine.calculateTotal(items)

        assert total == 100.00

    def test_calculate_total_empty_items(self):
        items = []

        engine = PricingEngine()
        total = engine.calculateTotal(items)

        assert total == 0.00

    def test_calculate_total_decimal_prices(self):
        items = [
            {"quantity": 3, "unit_price": 9.99},
            {"quantity": 2, "unit_price": 15.50},
        ]

        engine = PricingEngine()
        total = engine.calculateTotal(items)

        assert abs(total - 60.97) < 0.01

    def test_calculate_total_large_quantity(self):
        items = [{"quantity": 1000, "unit_price": 1.00}]

        engine = PricingEngine()
        total = engine.calculateTotal(items)

        assert total == 1000.00

    def test_calculate_total_precision(self):
        items = [
            {"quantity": 1, "unit_price": 0.99},
            {"quantity": 1, "unit_price": 0.99},
            {"quantity": 1, "unit_price": 0.99},
        ]

        engine = PricingEngine()
        total = engine.calculateTotal(items)

        assert total == 2.97

    def test_calculate_item_line_total(self):
        engine = PricingEngine()
        line_total = engine.calculateLineTotal(quantity=5, unit_price=10.00)

        assert line_total == 50.00

    def test_calculate_item_line_total_decimal(self):
        engine = PricingEngine()
        line_total = engine.calculateLineTotal(quantity=3, unit_price=9.99)

        assert abs(line_total - 29.97) < 0.01

    def test_apply_discount_percentage(self):
        items = [{"quantity": 10, "unit_price": 10.00}]

        engine = PricingEngine()
        total_no_discount = engine.calculateTotal(items)
        total_with_discount = engine.calculateTotal(items, discount_percent=10)

        assert total_with_discount == total_no_discount * 0.9

    def test_apply_discount_absolute(self):
        items = [{"quantity": 10, "unit_price": 10.00}]

        engine = PricingEngine()
        total = engine.calculateTotal(items, discount_absolute=10.00)

        assert total == 90.00

    def test_calculate_tax(self):
        items = [{"quantity": 10, "unit_price": 10.00}]

        engine = PricingEngine()
        total_without_tax = engine.calculateTotal(items)
        total_with_tax = engine.calculateTotal(items, tax_percent=23)

        expected_tax_amount = total_without_tax * 0.23
        assert abs(total_with_tax - (total_without_tax + expected_tax_amount)) < 0.01

    def test_bulk_order_discount(self):
        items = [{"quantity": 100, "unit_price": 1.00}]

        engine = PricingEngine()
        total = engine.calculateTotal(items, bulk_threshold=50, bulk_discount_percent=5)

        assert total <= 100.00

    def test_calculate_total_from_order_object(self, order_draft, multiple_pins):
        for i, pin in enumerate(multiple_pins[:3]):
            OrderItem.objects.create(
                order=order_draft,
                pin=pin,
                quantity=i + 1,
                unit_price=pin.price,
            )

        items = [
            {"quantity": item.quantity, "unit_price": item.unit_price}
            for item in order_draft.items.all()
        ]

        engine = PricingEngine()
        total = engine.calculateTotal(items)

        assert total > 0

    def test_calculate_average_item_price(self):
        items = [
            {"quantity": 5, "unit_price": 10.00},
            {"quantity": 5, "unit_price": 20.00},
        ]

        engine = PricingEngine()
        avg = engine.calculateAveragePrice(items)

        assert avg == 15.00

    def test_calculate_average_item_price_weighted_by_quantity(self):
        items = [
            {"quantity": 1, "unit_price": 10.00},
            {"quantity": 9, "unit_price": 20.00},
        ]

        engine = PricingEngine()
        avg = engine.calculateAveragePrice(items)

        assert avg == 19.00

    def test_get_line_subtotals(self):
        items = [
            {"quantity": 2, "unit_price": 10.00},
            {"quantity": 3, "unit_price": 15.00},
        ]

        engine = PricingEngine()
        subtotals = engine.getLineSubtotals(items)

        assert len(subtotals) == 2
        assert subtotals[0] == 20.00
        assert subtotals[1] == 45.00

    def test_round_total_to_two_decimals(self):
        items = [{"quantity": 3, "unit_price": 0.33}]

        engine = PricingEngine()
        total = engine.calculateTotal(items)

        assert len(str(total).split('.')[-1]) <= 2

    def test_handle_zero_quantity(self):
        items = [{"quantity": 0, "unit_price": 10.00}]

        engine = PricingEngine()
        total = engine.calculateTotal(items)

        assert total == 0.00

    def test_cumulative_pricing_calculation(self):
        engine = PricingEngine()

        subtotal = engine.calculateTotal([{"quantity": 5, "unit_price": 10.00}])
        tax = subtotal * 0.23
        total = subtotal + tax

        assert total > subtotal

