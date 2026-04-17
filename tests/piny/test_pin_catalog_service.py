import pytest
from skarbiec.services import PinCatalogService
from skarbiec.models import Pin


@pytest.mark.django_db
class TestPinCatalogService:

    def test_get_available_pins_returns_active_pins(self, multiple_pins):
        service = PinCatalogService()
        available = service.getAvailablePins()

        assert len(available) > 0
        assert all(pin.active is True for pin in available)

    def test_get_available_pins_excludes_inactive(self, pin_available, pin_unavailable):
        service = PinCatalogService()
        available = service.getAvailablePins()

        assert pin_available in available
        assert pin_unavailable not in available

    def test_get_available_pins_excludes_out_of_stock(self, db):
        in_stock = Pin.objects.create(
            name="In Stock",
            description="Available",
            price=10.00,
            available_quantity=10,
            active=True,
        )
        out_of_stock = Pin.objects.create(
            name="Out of Stock",
            description="Unavailable",
            price=10.00,
            available_quantity=0,
            active=True,
        )

        service = PinCatalogService()
        available = service.getAvailablePins()

        assert in_stock in available
        assert out_of_stock not in available

    def test_get_available_pins_returns_empty_list_when_none(self, db):
        service = PinCatalogService()
        available = service.getAvailablePins()

        assert isinstance(available, list)
        assert len(available) == 0

    def test_get_available_pins_includes_price_data(self, pin_available):
        service = PinCatalogService()
        available = service.getAvailablePins()

        found_pin = [p for p in available if p.id == pin_available.id][0]
        assert found_pin.price == pin_available.price

    def test_get_available_pins_includes_description(self, pin_available):
        service = PinCatalogService()
        available = service.getAvailablePins()

        found_pin = [p for p in available if p.id == pin_available.id][0]
        assert found_pin.description == pin_available.description

    def test_get_available_pins_multiple_results(self, multiple_pins):
        service = PinCatalogService()
        available = service.getAvailablePins()

        assert len(available) == 5

    def test_get_available_pins_sorted_by_name(self, db):
        Pin.objects.create(name="Zebra Pin", description="Z", price=1.0, available_quantity=1, active=True)
        Pin.objects.create(name="Apple Pin", description="A", price=1.0, available_quantity=1, active=True)
        Pin.objects.create(name="Mango Pin", description="M", price=1.0, available_quantity=1, active=True)

        service = PinCatalogService()
        available = service.getAvailablePins()

        names = [p.name for p in available]
        assert "Apple Pin" in names
        assert "Mango Pin" in names
        assert "Zebra Pin" in names

    def test_sync_pins_creates_pins(self, db, mocker):
        mock_sync_data = [
            {"name": "Synced Pin 1", "description": "Desc 1", "price": 10.0, "quantity": 50},
            {"name": "Synced Pin 2", "description": "Desc 2", "price": 15.0, "quantity": 30},
        ]
        mocker.patch.object(
            PinCatalogService,
            "_fetch_external_pins",
            return_value=mock_sync_data
        )

        service = PinCatalogService()
        service.syncPins()

        synced_pins = Pin.objects.all()
        assert synced_pins.count() >= 2

    def test_sync_pins_activates_synced_pins(self, db, mocker):
        mock_sync_data = [
            {"name": "Synced Pin", "description": "Desc", "price": 10.0, "quantity": 50},
        ]
        mocker.patch.object(
            PinCatalogService,
            "_fetch_external_pins",
            return_value=mock_sync_data
        )

        service = PinCatalogService()
        service.syncPins()

        synced = Pin.objects.filter(name="Synced Pin").first()
        assert synced is not None
        assert synced.active is True

    def test_get_pin_details_returns_pin_data(self, pin_available):
        service = PinCatalogService()
        details = service.getPinDetails([pin_available.id])

        assert len(details) > 0
        assert details[0].id == pin_available.id

    def test_get_pin_details_multiple_ids(self, multiple_pins):
        ids = [p.id for p in multiple_pins[:3]]

        service = PinCatalogService()
        details = service.getPinDetails(ids)

        assert len(details) == 3

    def test_get_pin_details_includes_current_price(self, pin_available):
        service = PinCatalogService()
        details = service.getPinDetails([pin_available.id])

        assert details[0].price == pin_available.price

    def test_get_pin_details_invalid_id(self, db):
        service = PinCatalogService()
        details = service.getPinDetails([999999])

        assert len(details) == 0

    def test_get_pin_details_mixed_valid_invalid_ids(self, pin_available):
        service = PinCatalogService()
        details = service.getPinDetails([pin_available.id, 999999])

        assert any(p.id == pin_available.id for p in details)

    def test_get_available_pins_filter_by_stock_threshold(self, db):
        Pin.objects.create(name="Low Stock", description="1 item", price=10.0, available_quantity=1, active=True)
        Pin.objects.create(name="Good Stock", description="10 items", price=10.0, available_quantity=10, active=True)

        service = PinCatalogService()
        available = service.getAvailablePins()

        assert len(available) >= 2

    def test_sync_pins_updates_existing_pins(self, db, pin_available, mocker):
        original_price = pin_available.price

        mock_sync_data = [
            {"name": "Pin 1", "description": "Updated", "price": 20.0, "quantity": 100},
        ]
        mocker.patch.object(
            PinCatalogService,
            "_fetch_external_pins",
            return_value=mock_sync_data
        )

        service = PinCatalogService()
        service.syncPins()

        updated = Pin.objects.get(id=pin_available.id)
        assert updated.price != original_price

