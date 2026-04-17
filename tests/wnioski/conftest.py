import pytest
from django.contrib.auth.models import User as DjangoUser


@pytest.fixture
def user(db):
    return DjangoUser.objects.create_user(
        username="kasztelan",
        email="kasztelan@org.pl",
        password="securepass",
    )


@pytest.fixture
def application_template(db):
    from wnioski.models import ApplicationTemplate
    return ApplicationTemplate.objects.create(
        name="Default Template",
        format="pdf",
        template_blob=b"PDFDATA",
    )


@pytest.fixture
def wniosek(db, user, application_template):
    from wnioski.models import Wniosek, Status
    return Wniosek.objects.create(
        user=user,
        status=Status.DRAFT,
        filled_data={"field1": "value1"},
        application_template=application_template,
    )


@pytest.fixture
def zarzadzenie_ssuj(db):
    from wnioski.models import ZarzadzenieSSUJ
    return ZarzadzenieSSUJ.objects.create(
        title="Order 1",
        content="Some content",
        date="2025-01-01",
    )

