import pytest
from django.contrib.auth.models import User as DjangoUser


@pytest.fixture
def wielu_mistrz_user(db):
    return DjangoUser.objects.create_user(
        username="wielu_mistrz",
        email="mistrz@org.pl",
        password="securepass",
    )


@pytest.fixture
def regular_user(db):
    return DjangoUser.objects.create_user(
        username="regularuser",
        email="regular@org.pl",
        password="securepass",
    )


@pytest.fixture
def zadanie_todo(db, wielu_mistrz_user):
    from dashboard.models import Zadanie
    return Zadanie.objects.create(
        tytul="Test Todo",
        opis="Test Description",
        warunki="Test Conditions",
        status="TODO",
        assigned_to=wielu_mistrz_user,
    )


@pytest.fixture
def zadanie_done(db, wielu_mistrz_user):
    from dashboard.models import Zadanie
    return Zadanie.objects.create(
        tytul="Completed Todo",
        opis="Completed Description",
        warunki="Completed Conditions",
        status="DONE",
        assigned_to=wielu_mistrz_user,
    )

