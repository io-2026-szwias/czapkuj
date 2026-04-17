"""
Tests for WydarzenieKalendarzowe (Calendar Event) model.
"""
import pytest
from datetime import datetime, date, timedelta


class TestWydarzenieKalendarzowe:
    """Tests for base calendar event model."""

    @pytest.mark.django_db
    def test_wydarzenie_kalendarzowe_has_nazwa_field(self):
        """WydarzenieKalendarzowe should have nazwa (name) field."""
        # Arrange
        from kalendarz.models import WydarzenieKalendarzowe

        # Act
        event = WydarzenieKalendarzowe.objects.create(
            nazwa="Test Event",
            data_rozpoczecia=date.today()
        )

        # Assert
        assert event.nazwa == "Test Event"

    @pytest.mark.django_db
    def test_wydarzenie_kalendarzowe_has_data_rozpoczecia_field(self):
        """WydarzenieKalendarzowe should have data_rozpoczecia (start date) field."""
        # Arrange
        from kalendarz.models import WydarzenieKalendarzowe
        start_date = date(2026, 5, 15)

        # Act
        event = WydarzenieKalendarzowe.objects.create(
            nazwa="Event",
            data_rozpoczecia=start_date
        )

        # Assert
        assert event.data_rozpoczecia == start_date

    @pytest.mark.django_db
    def test_wydarzenie_kalendarzowe_has_link_field(self):
        """WydarzenieKalendarzowe should have link (URL) field."""
        # Arrange
        from kalendarz.models import WydarzenieKalendarzowe

        # Act
        event = WydarzenieKalendarzowe.objects.create(
            nazwa="Event",
            data_rozpoczecia=date.today(),
            link="https://example.com/event"
        )

        # Assert
        assert event.link == "https://example.com/event"

    @pytest.mark.django_db
    def test_wydarzenie_kalendarzowe_has_opis_field(self):
        """WydarzenieKalendarzowe should have opis (description) field."""
        # Arrange
        from kalendarz.models import WydarzenieKalendarzowe

        # Act
        event = WydarzenieKalendarzowe.objects.create(
            nazwa="Event",
            data_rozpoczecia=date.today(),
            opis="Test description"
        )

        # Assert
        assert event.opis == "Test description"

    @pytest.mark.django_db
    def test_link_field_is_nullable(self):
        """link field should be nullable."""
        # Arrange
        from kalendarz.models import WydarzenieKalendarzowe

        # Act
        event = WydarzenieKalendarzowe.objects.create(
            nazwa="Event",
            data_rozpoczecia=date.today(),
            link=None
        )

        # Assert
        assert event.link is None

    @pytest.mark.django_db
    def test_opis_field_is_nullable(self):
        """opis field should be nullable."""
        # Arrange
        from kalendarz.models import WydarzenieKalendarzowe

        # Act
        event = WydarzenieKalendarzowe.objects.create(
            nazwa="Event",
            data_rozpoczecia=date.today(),
            opis=None
        )

        # Assert
        assert event.opis is None

    @pytest.mark.django_db
    def test_create_multiple_calendar_events(self):
        """Should be able to create multiple calendar events."""
        # Arrange
        from kalendarz.models import WydarzenieKalendarzowe

        # Act
        event1 = WydarzenieKalendarzowe.objects.create(
            nazwa="Event 1",
            data_rozpoczecia=date(2026, 5, 15)
        )
        event2 = WydarzenieKalendarzowe.objects.create(
            nazwa="Event 2",
            data_rozpoczecia=date(2026, 6, 20)
        )

        # Assert
        assert WydarzenieKalendarzowe.objects.count() == 2
        assert event1.nazwa == "Event 1"
        assert event2.nazwa == "Event 2"

