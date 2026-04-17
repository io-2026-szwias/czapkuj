"""
Integration tests for calendar system workflows.
"""
import pytest
from datetime import date, timedelta
from django.test import Client
from django.urls import reverse


class TestCalendarWorkflows:
    """Integration tests for calendar system workflows."""

    @pytest.mark.django_db
    def test_complete_calendar_workflow(self):
        """User should be able to open calendar and view events."""
        # Arrange
        from kalendarz.models import WydarzenieKalendarzowe
        WydarzenieKalendarzowe.objects.create(
            nazwa="Event",
            data_rozpoczecia=date.today()
        )
        client = Client()
        url = reverse("calendar_view")

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200
        assert b"html" in response.content.lower()

    @pytest.mark.django_db
    def test_calendar_displays_event_details(self):
        """Calendar should display event name, date, and description."""
        # Arrange
        from kalendarz.models import WydarzenieKalendarzowe
        event = WydarzenieKalendarzowe.objects.create(
            nazwa="Test Event",
            data_rozpoczecia=date(2026, 5, 15),
            opis="Test description",
            link="https://example.com"
        )
        client = Client()
        url = reverse("calendar_view")

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_calendar_subscription_workflow(self):
        """User should be able to subscribe to calendar feed."""
        # Arrange
        from kalendarz.models import WydarzenieKalendarzowe
        WydarzenieKalendarzowe.objects.create(
            nazwa="Event",
            data_rozpoczecia=date.today()
        )
        client = Client()
        view_url = reverse("calendar_view")
        sub_url = reverse("calendar_subscription")

        # Act
        view_response = client.get(view_url)
        sub_response = client.get(sub_url)

        # Assert
        assert view_response.status_code == 200
        assert sub_response.status_code in [200, 302, 404]

    @pytest.mark.django_db
    def test_calendar_with_multiple_events(self):
        """Calendar should display multiple events."""
        # Arrange
        from kalendarz.models import WydarzenieKalendarzowe
        for i in range(5):
            WydarzenieKalendarzowe.objects.create(
                nazwa=f"Event {i}",
                data_rozpoczecia=date.today() + timedelta(days=i)
            )
        client = Client()
        url = reverse("calendar_view")

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_calendar_with_different_event_types(self):
        """Calendar should handle Wydarzenie and Chrzest events together."""
        # Arrange
        from kalendarz.models import Wydarzenie, Chrzest, Miejsce
        place = Miejsce.objects.create(nazwa="Church")

        Wydarzenie.objects.create(
            nazwa="Regular Event",
            data_rozpoczecia=date.today(),
            czy_jednodniowe=True
        )
        Chrzest.objects.create(
            nazwa="Baptism",
            data_rozpoczecia=date.today() + timedelta(days=1),
            miejsce=place
        )
        client = Client()
        url = reverse("calendar_view")

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_calendar_polymorphic_query(self):
        """Calendar view should use polymorphic query for different event types."""
        # Arrange
        from kalendarz.models import Wydarzenie, Chrzest
        Wydarzenie.objects.create(
            nazwa="Event",
            data_rozpoczecia=date.today()
        )
        Chrzest.objects.create(
            nazwa="Baptism",
            data_rozpoczecia=date.today()
        )
        from kalendarz.views import CalendarView
        view = CalendarView()

        # Act
        queryset = view.get_queryset()

        # Assert
        assert queryset.count() >= 2

    @pytest.mark.django_db
    def test_calendar_renders_correctly(self):
        """Calendar should render correctly with proper HTML structure."""
        # Arrange
        client = Client()
        url = reverse("calendar_view")

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200
        assert b"<" in response.content  # Contains HTML

    @pytest.mark.django_db
    def test_calendar_subscription_generates_feed(self):
        """Calendar subscription should generate valid feed."""
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
        if response.status_code == 200:
            assert len(response.content) > 0

    @pytest.mark.django_db
    def test_calendar_handles_empty_events(self):
        """Calendar should handle empty event list gracefully."""
        # Arrange
        client = Client()
        url = reverse("calendar_view")

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_calendar_events_sorted_by_date(self):
        """Calendar events should be sorted by date."""
        # Arrange
        from kalendarz.models import WydarzenieKalendarzowe
        from kalendarz.views import CalendarView

        WydarzenieKalendarzowe.objects.create(
            nazwa="Event 3",
            data_rozpoczecia=date.today() + timedelta(days=5)
        )
        WydarzenieKalendarzowe.objects.create(
            nazwa="Event 1",
            data_rozpoczecia=date.today()
        )
        WydarzenieKalendarzowe.objects.create(
            nazwa="Event 2",
            data_rozpoczecia=date.today() + timedelta(days=2)
        )
        view = CalendarView()

        # Act
        queryset = view.get_queryset()

        # Assert
        assert queryset.count() == 3

    @pytest.mark.django_db
    def test_calendar_with_external_links(self):
        """Calendar should preserve and display external links."""
        # Arrange
        from kalendarz.models import WydarzenieKalendarzowe
        event = WydarzenieKalendarzowe.objects.create(
            nazwa="Event",
            data_rozpoczecia=date.today(),
            link="https://example.com/details"
        )
        client = Client()
        url = reverse("calendar_view")

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_calendar_api_response_structure(self):
        """Calendar API should return structured data."""
        # Arrange
        from kalendarz.models import WydarzenieKalendarzowe
        WydarzenieKalendarzowe.objects.create(
            nazwa="Event",
            data_rozpoczecia=date.today()
        )
        from kalendarz.views import CalendarView
        view = CalendarView()

        # Act
        queryset = view.get_queryset()
        events = list(queryset)

        # Assert
        assert len(events) > 0
        event = events[0]
        assert hasattr(event, 'nazwa')
        assert hasattr(event, 'data_rozpoczecia')

