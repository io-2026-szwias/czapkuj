import pytest
from wnioski.models import Wniosek, ApplicationTemplate, Status, ZarzadzenieSSUJ

@pytest.mark.django_db
class TestWniosekModel:
    def test_wniosek_create_with_required_fields(self, user, application_template):
        wniosek = Wniosek.objects.create(
            user=user,
            status=Status.DRAFT,
            filled_data={"field": "value"},
            application_template=application_template,
        )
        assert wniosek.id is not None
        assert wniosek.status == Status.DRAFT
        assert wniosek.application_template == application_template

    def test_wniosek_status_transitions(self, wniosek):
        wniosek.status = Status.SUBMITTED
        wniosek.save()
        updated = Wniosek.objects.get(id=wniosek.id)
        assert updated.status == Status.SUBMITTED

    def test_wniosek_filled_data_is_stored(self, wniosek):
        assert isinstance(wniosek.filled_data, dict)
        assert "field1" in wniosek.filled_data

    def test_wniosek_has_creation_date(self, wniosek):
        assert wniosek.data_utworzenia is not None

    def test_wniosek_links_to_user(self, wniosek, user):
        assert wniosek.user == user

    def test_wniosek_links_to_template(self, wniosek, application_template):
        assert wniosek.application_template == application_template

@pytest.mark.django_db
class TestApplicationTemplateModel:
    def test_template_create_with_required_fields(self):
        template = ApplicationTemplate.objects.create(
            name="Test Template",
            format="pdf",
            template_blob=b"PDFDATA",
        )
        assert template.id is not None
        assert template.format == "pdf"

    def test_template_fill_template_method(self, application_template):
        data = {"field": "value"}
        filled = application_template.fillTemplate(data)
        assert filled is not None

    def test_template_blob_is_stored(self, application_template):
        assert application_template.template_blob is not None

@pytest.mark.django_db
class TestZarzadzenieSSUJModel:
    def test_zarzadzenie_create_with_required_fields(self):
        zarz = ZarzadzenieSSUJ.objects.create(
            title="Order 1",
            content="Some content",
            date="2025-01-01",
        )
        assert zarz.id is not None
        assert zarz.title == "Order 1"
        assert zarz.content == "Some content"
        assert zarz.date == "2025-01-01"

