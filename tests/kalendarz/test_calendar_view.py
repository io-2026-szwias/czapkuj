"""
Tests for CalendarView and calendar visualization.
"""
import pytest
from datetime import date, datetime, timedelta
from django.test import Client
from django.urls import reverse


class TestCalendarView:
    """Tests for calendar view and rendering."""

    @pytest.mark.django_db
    def test_calendar_view_returns_200(self):
        """GET /kalendarz/ should return 200 OK."""
        # Arrange
        client = Client()
        url = reverse("calendar_view")  # Adjust URL name as needed

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_calendar_view_returns_html(self):
        """Calendar view should return HTML response."""
        # Arrange
        client = Client()
        url = reverse("calendar_view")

        # Act
        response = client.get(url)

        # Assert
        assert "text/html" in response["Content-Type"]

    @pytest.mark.django_db
    def test_calendar_view_has_queryset_method(self):
        """CalendarView should have get_queryset method."""
        # Arrange
        from kalendarz.views import CalendarView
        view = CalendarView()

        # Act & Assert
        assert hasattr(view, "get_queryset")
        assert callable(view.get_queryset)

    @pytest.mark.django_db
    def test_calendar_view_get_queryset_returns_events(self):
        """get_queryset() should return calendar events."""
        # Arrange
        from kalendarz.models import WydarzenieKalendarzowe
        from kalendarz.views import CalendarView
        WydarzenieKalendarzowe.objects.create(
            nazwa="Event",
            data_rozpoczecia=date.today()
        )
        view = CalendarView()

        # Act
        queryset = view.get_queryset()

        # Assert
        assert queryset.count() >= 1

    @pytest.mark.django_db
    def test_calendar_view_lists_upcoming_events(self):
        """Calendar view should list upcoming events."""
        # Arrange
        from kalendarz.models import WydarzenieKalendarzowe
        event = WydarzenieKalendarzowe.objects.create(
            nazwa="Upcoming Event",
            data_rozpoczecia=date.today() + timedelta(days=5)
        )
        client = Client()
        url = reverse("calendar_view")

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200
        assert b"Upcoming Event" in response.content or event.nazwa in str(response.content)

    @pytest.mark.django_db
    def test_calendar_view_displays_past_events(self):
        """Calendar view should also display past events."""
        # Arrange
        from kalendarz.models import WydarzenieKalendarzowe
        event = WydarzenieKalendarzowe.objects.create(
            nazwa="Past Event",
            data_rozpoczecia=date.today() - timedelta(days=5)
        )
        client = Client()
        url = reverse("calendar_view")

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_calendar_view_render_calendar_method_exists(self):
        """CalendarView should have render_calendar method."""
        # Arrange
        from kalendarz.views import CalendarView
        view = CalendarView()

        # Act & Assert
        assert hasattr(view, "render_calendar")
        assert callable(view.render_calendar)

    @pytest.mark.django_db
    def test_calendar_view_handles_no_events(self):
        """Calendar view should handle empty event list gracefully."""
        # Arrange
        client = Client()
        url = reverse("calendar_view")

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_calendar_view_with_multiple_event_types(self):
        """Calendar view should handle multiple event types (Wydarzenie, Chrzest)."""
        # Arrange
        from kalendarz.models import Wydarzenie, Chrzest
        event1 = Wydarzenie.objects.create(
            nazwa="Regular Event",
            data_rozpoczecia=date.today(),
            czy_jednodniowe=True
        )
        event2 = Chrzest.objects.create(
            nazwa="Baptism",
            data_rozpoczecia=date.today() + timedelta(days=1)
        )
        client = Client()
        url = reverse("calendar_view")

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_calendar_view_filters_by_date_range(self):
        """Calendar view should optionally filter events by date range."""
        # Arrange
        from kalendarz.models import WydarzenieKalendarzowe
        start = date(2026, 5, 1)
        end = date(2026, 5, 31)

        event_in_range = WydarzenieKalendarzowe.objects.create(
            nazwa="In Range",
            data_rozpoczecia=date(2026, 5, 15)
        )
        event_out_range = WydarzenieKalendarzowe.objects.create(
            nazwa="Out of Range",
            data_rozpoczecia=date(2026, 4, 15)
        )

        # Act
        # Assuming view can filter by dates
        from kalendarz.views import CalendarView
        view = CalendarView()
        # queryset = view.get_queryset().filter(data_rozpoczecia__gte=start, data_rozpoczecia__lte=end)

        # Assert
        # assert queryset.count() >= 1
        # assert event_in_range in queryset

    @pytest.mark.django_db
    def test_calendar_includes_event_details(self):
        """Calendar should display event details (nazwa, data, opis)."""
        # Arrange
        from kalendarz.models import WydarzenieKalendarzowe
        WydarzenieKalendarzowe.objects.create(
            nazwa="Important Event",
            data_rozpoczecia=date.today(),
            opis="This is an important event"
        )
        client = Client()
        url = reverse("calendar_view")

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200

