"""
Pytest configuration and fixtures for Kalendarz tests.
"""
import pytest
from datetime import date, timedelta


@pytest.fixture
def sample_event(db):
    """Create a sample calendar event."""
    from kalendarz.models import WydarzenieKalendarzowe
    return WydarzenieKalendarzowe.objects.create(
        nazwa="Sample Event",
        data_rozpoczecia=date.today(),
        opis="Sample description"
    )


@pytest.fixture
def sample_place(db):
    """Create a sample place."""
    from kalendarz.models import Miejsce
    return Miejsce.objects.create(nazwa="Sample Church")


@pytest.fixture
def sample_person(db):
    """Create a sample person."""
    from kalendarz.models import Osoba
    return Osoba.objects.create(imie="John", nazwisko="Doe")


@pytest.fixture
def sample_baptism(db, sample_place):
    """Create a sample baptism event."""
    from kalendarz.models import Chrzest
    return Chrzest.objects.create(
        nazwa="Sample Baptism",
        data_rozpoczecia=date.today(),
        miejsce=sample_place
    )


@pytest.fixture
def sample_event_type(db):
    """Create a sample event type."""
    from kalendarz.models import TypWydarzenia
    return TypWydarzenia.objects.create(typ="Service")


@pytest.fixture
def sample_trip_type(db):
    """Create a sample trip type."""
    from kalendarz.models import TypWyjazdu
    return TypWyjazdu.objects.create(typ="Pilgrimage")


@pytest.fixture
def multiple_events(db):
    """Create multiple calendar events."""
    from kalendarz.models import WydarzenieKalendarzowe
    events = []
    for i in range(5):
        event = WydarzenieKalendarzowe.objects.create(
            nazwa=f"Event {i}",
            data_rozpoczecia=date.today() + timedelta(days=i)
        )
        events.append(event)
    return events


@pytest.fixture
def multiple_baptisms(db, sample_place):
    """Create multiple baptism events."""
    from kalendarz.models import Chrzest
    baptisms = []
    for i in range(3):
        baptism = Chrzest.objects.create(
            nazwa=f"Baptism {i}",
            data_rozpoczecia=date.today() + timedelta(days=i),
            miejsce=sample_place
        )
        baptisms.append(baptism)
    return baptisms


@pytest.fixture
def mixed_events(db, sample_place):
    """Create a mix of different event types."""
    from kalendarz.models import Wydarzenie, Chrzest
    events = {
        'events': [],
        'baptisms': []
    }

    for i in range(3):
        event = Wydarzenie.objects.create(
            nazwa=f"Event {i}",
            data_rozpoczecia=date.today() + timedelta(days=i),
            czy_jednodniowe=True
        )
        events['events'].append(event)

    for i in range(2):
        baptism = Chrzest.objects.create(
            nazwa=f"Baptism {i}",
            data_rozpoczecia=date.today() + timedelta(days=i),
            miejsce=sample_place
        )
        events['baptisms'].append(baptism)

    return events

