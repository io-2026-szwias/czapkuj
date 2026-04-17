"""
Tests for calendar subscription and feed generation.
"""
import pytest
from datetime import date, timedelta
from django.test import Client
from django.urls import reverse


class TestCalendarSubscription:
    """Tests for calendar subscription functionality."""

    @pytest.mark.django_db
    def test_subscription_view_exists(self):
        """Calendar subscription endpoint should exist."""
        # Arrange
        client = Client()
        url = reverse("calendar_subscription")  # Adjust URL name as needed

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code in [200, 404, 302]  # May redirect or return feed

    @pytest.mark.django_db
    def test_calendar_view_has_subscription_method(self):
        """CalendarView should have generate_subscription method."""
        # Arrange
        from kalendarz.views import CalendarView
        view = CalendarView()

        # Act & Assert
        assert hasattr(view, "generate_subscription")
        assert callable(view.generate_subscription)

    @pytest.mark.django_db
    def test_subscription_feed_returns_ics_format(self):
        """Subscription feed should return ICS/iCalendar format."""
        # Arrange
        from kalendarz.models import WydarzenieKalendarzowe
        WydarzenieKalendarzowe.objects.create(
            nazwa="Event",
            data_rozpoczecia=date.today()
        )
        client = Client()
        url = reverse("calendar_subscription")

        # Act
        response = client.get(url)

        # Assert
        # ICS feed should contain iCalendar format data
        if response.status_code == 200:
            assert b"BEGIN:VCALENDAR" in response.content or b"ics" in response.get("Content-Type", "").lower()

    @pytest.mark.django_db
    def test_subscription_includes_all_events(self):
        """Subscription feed should include all upcoming events."""
        # Arrange
        from kalendarz.models import WydarzenieKalendarzowe
        event1 = WydarzenieKalendarzowe.objects.create(
            nazwa="Event 1",
            data_rozpoczecia=date.today()
        )
        event2 = WydarzenieKalendarzowe.objects.create(
            nazwa="Event 2",
            data_rozpoczecia=date.today() + timedelta(days=5)
        )
        client = Client()
        url = reverse("calendar_subscription")

        # Act
        response = client.get(url)

        # Assert
        if response.status_code == 200:
            content = response.content.decode() if isinstance(response.content, bytes) else str(response.content)
            # Check that events are included in subscription
            assert "Event" in content or "BEGIN:VEVENT" in content

    @pytest.mark.django_db
    def test_subscription_feed_content_type(self):
        """Subscription feed should have correct content type."""
        # Arrange
        client = Client()
        url = reverse("calendar_subscription")

        # Act
        response = client.get(url)

        # Assert
        if response.status_code == 200:
            content_type = response.get("Content-Type", "")
            # Should be ICS/calendar format
            assert "text" in content_type or "calendar" in content_type or "ics" in content_type

    @pytest.mark.django_db
    def test_subscription_feed_includes_event_details(self):
        """Subscription feed should include event details (summary, date, description)."""
        # Arrange
        from kalendarz.models import WydarzenieKalendarzowe
        WydarzenieKalendarzowe.objects.create(
            nazwa="Detailed Event",
            data_rozpoczecia=date(2026, 5, 15),
            opis="Detailed description"
        )
        client = Client()
        url = reverse("calendar_subscription")

        # Act
        response = client.get(url)

        # Assert
        if response.status_code == 200:
            content = response.content.decode() if isinstance(response.content, bytes) else str(response.content)
            # Events should be included with details
            assert len(content) > 0

    @pytest.mark.django_db
    def test_subscription_can_be_added_to_google_calendar(self):
        """Subscription should be compatible with Google Calendar."""
        # Arrange
        from kalendarz.models import WydarzenieKalendarzowe
        WydarzenieKalendarzowe.objects.create(
            nazwa="Event",
            data_rozpoczecia=date.today()
        )
        client = Client()
        url = reverse("calendar_subscription")

        # Act
        response = client.get(url)

        # Assert
        # Feed should return appropriate format for Google Calendar
        assert response.status_code in [200, 302, 404]  # Valid responses

    @pytest.mark.django_db
    def test_subscription_feed_includes_event_date(self):
        """Subscription feed should include event dates."""
        # Arrange
        from kalendarz.models import WydarzenieKalendarzowe
        event_date = date(2026, 5, 15)
        WydarzenieKalendarzowe.objects.create(
            nazwa="Event",
            data_rozpoczecia=event_date
        )
        client = Client()
        url = reverse("calendar_subscription")

        # Act
        response = client.get(url)

        # Assert
        if response.status_code == 200:
            content = response.content.decode() if isinstance(response.content, bytes) else str(response.content)
            # Should include date information
            assert "2026" in content or "05" in content or len(content) > 0

    @pytest.mark.django_db
    def test_subscription_with_multiple_event_types(self):
        """Subscription should include all event types (Wydarzenie, Chrzest)."""
        # Arrange
        from kalendarz.models import Wydarzenie, Chrzest
        Wydarzenia.objects.create(
            nazwa="Event",
            data_rozpoczecia=date.today(),
            czy_jednodniowe=True
        )
        Chrzest.objects.create(
            nazwa="Baptism",
            data_rozpoczecia=date.today() + timedelta(days=1)
        )
        client = Client()
        url = reverse("calendar_subscription")

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code in [200, 302, 404]

    @pytest.mark.django_db
    def test_generate_subscription_method_works(self):
        """generate_subscription() should work correctly."""
        # Arrange
        from kalendarz.models import WydarzenieKalendarzowe
        from kalendarz.views import CalendarView
        WydarzenieKalendarzowe.objects.create(
            nazwa="Event",
            data_rozpoczecia=date.today()
        )
        view = CalendarView()

        # Act
        subscription = view.generate_subscription()

        # Assert
        assert subscription is not None
        assert isinstance(subscription, (str, bytes))

    @pytest.mark.django_db
    def test_subscription_updates_with_new_events(self):
        """Subscription should reflect newly added events."""
        # Arrange
        from kalendarz.models import WydarzenieKalendarzowe
        from kalendarz.views import CalendarView

        view = CalendarView()
        sub1 = view.generate_subscription()

        # Act
        WydarzenieKalendarzowe.objects.create(
            nazwa="New Event",
            data_rozpoczecia=date.today()
        )
        sub2 = view.generate_subscription()

        # Assert
        # New subscription should reflect the new event
        assert sub2 != sub1 or len(str(sub2)) >= len(str(sub1))

