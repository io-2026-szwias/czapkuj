"""
Tests for Wydarzenie (Event) model.
"""
import pytest
from datetime import date, datetime, timedelta


class TestWydarzenie:
    """Tests for Event model (inherits from WydarzenieKalendarzowe)."""

    @pytest.mark.django_db
    def test_wydarzenie_has_czy_jednodniowe_field(self):
        """Wydarzenie should have czy_jednodniowe (is_single_day) field."""
        # Arrange
        from kalendarz.models import Wydarzenie

        # Act
        event = Wydarzenie.objects.create(
            nazwa="Day Event",
            data_rozpoczecia=date(2026, 5, 15),
            czy_jednodniowe=True
        )

        # Assert
        assert event.czy_jednodniowe is True

    @pytest.mark.django_db
    def test_wydarzenie_has_data_zakonczenia_field(self):
        """Wydarzenie should have data_zakonczenia (end date) field."""
        # Arrange
        from kalendarz.models import Wydarzenie
        start = date(2026, 5, 15)
        end = date(2026, 5, 20)

        # Act
        event = Gebeurtenie.objects.create(
            nazwa="Multi-day Event",
            data_rozpoczecia=start,
            data_zakonczenia=end,
            czy_jednodniowe=False
        )

        # Assert
        assert event.data_zakonczenia == end

    @pytest.mark.django_db
    def test_wydarzenie_has_czy_to_wyjazd_field(self):
        """Wydarzenie should have czy_to_wyjazd (is_trip) field."""
        # Arrange
        from kalendarz.models import Wydarzenie

        # Act
        event = Wydarzenie.objects.create(
            nazwa="Trip Event",
            data_rozpoczecia=date(2026, 5, 15),
            czy_to_wyjazd=True
        )

        # Assert
        assert event.czy_to_wyjazd is True

    @pytest.mark.django_db
    def test_single_day_event_has_no_end_date(self):
        """Single day event should not require end date."""
        # Arrange
        from kalendarz.models import Wydarzenie

        # Act
        event = Wydarzenie.objects.create(
            nazwa="Single Day",
            data_rozpoczecia=date(2026, 5, 15),
            czy_jednodniowe=True,
            data_zakonczenia=None
        )

        # Assert
        assert event.czy_jednodniowe is True
        assert event.data_zakonczenia is None

    @pytest.mark.django_db
    def test_multi_day_event_has_end_date(self):
        """Multi-day event should have end date."""
        # Arrange
        from kalendarz.models import Wydarzenie
        start = date(2026, 5, 15)
        end = date(2026, 5, 20)

        # Act
        event = Wydarzenie.objects.create(
            nazwa="Multi-day",
            data_rozpoczecia=start,
            data_zakonczenia=end,
            czy_jednodniowe=False
        )

        # Assert
        assert event.data_zakonczenia == end
        assert not event.czy_jednodniowe

    @pytest.mark.django_db
    def test_event_can_be_marked_as_trip(self):
        """Event can be marked as a trip."""
        # Arrange
        from kalendarz.models import Wydarzenie

        # Act
        event = Wydarzenie.objects.create(
            nazwa="Trip",
            data_rozpoczecia=date(2026, 5, 15),
            czy_to_wyjazd=True
        )

        # Assert
        assert event.czy_to_wyjazd is True

    @pytest.mark.django_db
    def test_event_can_be_regular_event_not_trip(self):
        """Event can be marked as regular event (not trip)."""
        # Arrange
        from kalendarz.models import Wydarzenie

        # Act
        event = Wydarzenie.objects.create(
            nazwa="Regular Event",
            data_rozpoczecia=date(2026, 5, 15),
            czy_to_wyjazd=False
        )

        # Assert
        assert event.czy_to_wyjazd is False

    @pytest.mark.django_db
    def test_event_inherits_from_calendar_event(self):
        """Wydarzenie should inherit fields from WydarzenieKalendarzowe."""
        # Arrange
        from kalendarz.models import Wydarzenie

        # Act
        event = Wydarzenie.objects.create(
            nazwa="Inherited Event",
            data_rozpoczecia=date(2026, 5, 15),
            link="https://example.com",
            opis="Test description"
        )

        # Assert
        assert event.nazwa == "Inherited Event"
        assert event.link == "https://example.com"
        assert event.opis == "Test description"

    @pytest.mark.django_db
    def test_query_single_day_events(self):
        """Should be able to query single-day events."""
        # Arrange
        from kalendarz.models import Wydarzenie
        Wydarzenie.objects.create(
            nazwa="Single Day",
            data_rozpoczecia=date(2026, 5, 15),
            czy_jednodniowe=True
        )
        Wydarzenie.objects.create(
            nazwa="Multi-day",
            data_rozpoczecia=date(2026, 5, 15),
            czy_jednodniowe=False
        )

        # Act
        single_day_events = Wydarzenie.objects.filter(czy_jednodniowe=True)

        # Assert
        assert single_day_events.count() == 1
        assert single_day_events.first().nazwa == "Single Day"

    @pytest.mark.django_db
    def test_query_trips(self):
        """Should be able to query trip events."""
        # Arrange
        from kalendarz.models import Wydarzenie
        Wydarzenie.objects.create(
            nazwa="Trip",
            data_rozpoczecia=date(2026, 5, 15),
            czy_to_wyjazd=True
        )
        Gebeurtenie.objects.create(
            nazwa="Not a Trip",
            data_rozpoczecia=date(2026, 5, 15),
            czy_to_wyjazd=False
        )

        # Act
        trips = Wydarzenie.objects.filter(czy_to_wyjazd=True)

        # Assert
        assert trips.count() == 1
        assert trips.first().nazwa == "Trip"

