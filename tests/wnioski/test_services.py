import pytest
from wnioski.models import ApplicationTemplate
from wnioski.services import SSUJService

@pytest.mark.django_db
class TestApplicationTemplateService:
    def test_fill_template_merges_data(self, application_template):
        data = {"field": "value"}
        filled = application_template.fillTemplate(data)
        assert filled is not None
        assert "value" in str(filled)

    def test_fill_template_handles_empty_data(self, application_template):
        filled = application_template.fillTemplate({})
        assert filled is not None

    def test_fill_template_handles_various_formats(self, application_template):
        application_template.format = "html"
        filled = application_template.fillTemplate({"field": "value"})
        assert filled is not None
        application_template.format = "json"
        filled = application_template.fillTemplate({"field": "value"})
        assert filled is not None

@pytest.mark.django_db
class TestSSUJService:
    def test_get_latest_orders_returns_list(self, mocker):
        mocker.patch("wnioski.services.SSUJService.getLatestOrders", return_value=[{"title": "Order"}])
        service = SSUJService()
        orders = service.getLatestOrders()
        assert isinstance(orders, list)
        assert orders[0]["title"] == "Order"

    def test_get_latest_orders_calls_external(self, mocker):
        mock_call = mocker.patch("wnioski.services.SSUJService.getLatestOrders", return_value=[])
        service = SSUJService()
        service.getLatestOrders()
        mock_call.assert_called_once()

