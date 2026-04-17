"""
Pytest configuration and fixtures for Mapa tests.
"""
import pytest


@pytest.fixture
def sample_place(db):
    """Create a sample place."""
    from mapa.models import Miejsce
    return Miejsce.objects.create(
        nazwa="Sample Place",
        adres="Sample Address",
        latitude=52.2297,
        longitude=21.0122
    )


@pytest.fixture
def sample_place_type(db):
    """Create a sample place type."""
    from mapa.models import TypMiejsca
    return TypMiejsca.objects.create(nazwa="Library", emoji="📚")


@pytest.fixture
def sample_discount(db, sample_place):
    """Create a sample discount."""
    from mapa.models import Znizka
    return Znizka.objects.create(
        dzien_tygodnia="Monday",
        opis="Monday discount - 20% off",
        miejsce=sample_place
    )


@pytest.fixture
def place_with_type_and_discount(db, sample_place_type):
    """Create a place with type and discounts."""
    from mapa.models import Miejsce, Znizka
    place = Miejsce.objects.create(
        nazwa="Library",
        adres="Main Street",
        typ_miejsca=sample_place_type,
        latitude=52.2297,
        longitude=21.0122
    )
    Znizka.objects.create(dzien_tygodnia="Monday", opis="Discount 1", miejsce=place)
    Znizka.objects.create(dzien_tygodnia="Friday", opis="Discount 2", miejsce=place)
    return place


@pytest.fixture
def multiple_places(db):
    """Create multiple places."""
    from mapa.models import Miejsce
    places = []
    for i in range(5):
        place = Miejsce.objects.create(
            nazwa=f"Place {i}",
            adres=f"Address {i}",
            latitude=52.2297 + (i * 0.01),
            longitude=21.0122 + (i * 0.01)
        )
        places.append(place)
    return places


@pytest.fixture
def multiple_place_types(db):
    """Create multiple place types."""
    from mapa.models import TypMiejsca
    types = []
    type_data = [
        ("Library", "📚"),
        ("Park", "🌳"),
        ("Cafe", "☕"),
        ("Museum", "🏛️"),
    ]
    for name, emoji in type_data:
        place_type = TypMiejsca.objects.create(nazwa=name, emoji=emoji)
        types.append(place_type)
    return types


@pytest.fixture
def places_with_types(db, multiple_place_types):
    """Create places assigned to different types."""
    from mapa.models import Miejsce
    places = {}
    for i, place_type in enumerate(multiple_place_types):
        place = Miejsce.objects.create(
            nazwa=f"{place_type.nazwa} {i}",
            adres=f"Address {i}",
            typ_miejsca=place_type,
            latitude=52.2297 + (i * 0.01),
            longitude=21.0122 + (i * 0.01)
        )
        places[place_type.nazwa] = place
    return places


@pytest.fixture
def places_with_discounts_by_day(db):
    """Create places with discounts for different days."""
    from mapa.models import Miejsce, Znizka

    places = {}
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    for day in days:
        place = Miejsce.objects.create(
            nazwa=f"{day} Place",
            adres=f"{day} Address",
            latitude=52.2297,
            longitude=21.0122
        )
        Znizka.objects.create(
            dzien_tygodnia=day,
            opis=f"{day} discount",
            miejsce=place
        )
        places[day] = place

    return places


@pytest.fixture
def complex_map_setup(db, multiple_place_types):
    """Create a complex map setup with many places, types, and discounts."""
    from mapa.models import Miejsce, Znizka

    setup = {
        'places': [],
        'discounts': [],
        'by_type': {}
    }

    for i, place_type in enumerate(multiple_place_types):
        for j in range(3):
            place = Miejsce.objects.create(
                nazwa=f"{place_type.nazwa} {j}",
                adres=f"Address {i}-{j}",
                typ_miejsca=place_type,
                latitude=52.2297 + (i * 0.01) + (j * 0.001),
                longitude=21.0122 + (i * 0.01) + (j * 0.001)
            )
            setup['places'].append(place)

            if j % 2 == 0:  # Add discounts to some places
                discount = Znizka.objects.create(
                    dzien_tygodnia=["Monday", "Wednesday", "Friday"][j % 3],
                    opis=f"Discount for {place.nazwa}",
                    miejsce=place
                )
                setup['discounts'].append(discount)

        setup['by_type'][place_type.nazwa] = [p for p in setup['places'] if p.typ_miejsca == place_type]

    return setup

