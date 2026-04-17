import pytest
from django.contrib.auth.models import User as DjangoUser


@pytest.fixture
def user(db):
    return DjangoUser.objects.create_user(
        username="member",
        email="member@org.pl",
        password="securepass",
    )


@pytest.fixture
def pin_available(db):
    from skarbiec.models import Pin
    return Pin.objects.create(
        name="Pin 1",
        description="First Belgian Pin",
        price=10.99,
        available_quantity=50,
        active=True,
    )


@pytest.fixture
def pin_unavailable(db):
    from skarbiec.models import Pin
    return Pin.objects.create(
        name="Pin 2",
        description="Second Pin - Out of stock",
        price=15.50,
        available_quantity=0,
        active=False,
    )


@pytest.fixture
def pin_expensive(db):
    from skarbiec.models import Pin
    return Pin.objects.create(
        name="Premium Pin",
        description="Expensive Belgian Pin",
        price=99.99,
        available_quantity=5,
        active=True,
    )


@pytest.fixture
def multiple_pins(db):
    from skarbiec.models import Pin
    pins = []
    for i in range(5):
        pin = Pin.objects.create(
            name=f"Pin {i}",
            description=f"Belgian Pin {i}",
            price=float(10 + i * 5),
            available_quantity=10 + i,
            active=True,
        )
        pins.append(pin)
    return pins


@pytest.fixture
def order_draft(db, user):
    from skarbiec.models import Order
    return Order.objects.create(
        created_by=user,
        status="DRAFT",
        total_cost=0.00,
    )


@pytest.fixture
def order_submitted(db, user):
    from skarbiec.models import Order
    return Order.objects.create(
        created_by=user,
        status="SUBMITTED",
        total_cost=50.00,
    )


@pytest.fixture
def order_paid(db, user):
    from skarbiec.models import Order
    return Order.objects.create(
        created_by=user,
        status="PAID",
        total_cost=50.00,
    )

