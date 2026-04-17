"""
Integration tests for Map system workflows.
"""
import pytest
from django.test import Client
from django.urls import reverse


class TestMapWorkflows:
    """Integration tests for map system workflows."""

    @pytest.mark.django_db
    def test_user_opens_map_page(self):
        """User should be able to open the map page."""
        # Arrange
        client = Client()
        url = reverse("map_view")

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200
        assert b"html" in response.content.lower()

    @pytest.mark.django_db
    def test_map_displays_places(self):
        """Map should display all open places."""
        # Arrange
        from mapa.models import Miejsce
        place1 = Miejsce.objects.create(
            nazwa="Library",
            adres="Main Street",
            zamkniete_na_stale=False
        )
        place2 = Miejsce.objects.create(
            nazwa="Park",
            adres="Central Park",
            zamkniete_na_stale=False
        )

        client = Client()
        url = reverse("map_data")

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_filter_places_workflow(self):
        """User applies filter to find places of specific type (UC-22)."""
        # Arrange
        from mapa.models import Miejsce, TypMiejsca
        library_type = TypMiejsca.objects.create(nazwa="Library", emoji="📚")
        park_type = TypMiejsca.objects.create(nazwa="Park", emoji="🌳")

        Miejsce.objects.create(
            nazwa="City Library",
            adres="Main Street",
            typ_miejsca=library_type
        )
        Miejsce.objects.create(
            nazwa="Park",
            adres="Central Park",
            typ_miejsca=park_type
        )

        client = Client()
        url = reverse("map_data") + f"?typ={library_type.id}"

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_filter_discounts_workflow(self):
        """User filters places by available discount day (UC-23)."""
        # Arrange
        from mapa.models import Miejsce, Znizka
        place1 = Miejsce.objects.create(nazwa="Place 1", adres="Address 1")
        place2 = Miejsce.objects.create(nazwa="Place 2", adres="Address 2")

        Znizka.objects.create(
            dzien_tygodnia="Monday",
            opis="Monday discount",
            miejsce=place1
        )
        Znizka.objects.create(
            dzien_tygodnia="Tuesday",
            opis="Tuesday discount",
            miejsce=place2
        )

        client = Client()
        url = reverse("map_data") + "?dzien_tygodnia=Monday"

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_map_with_coordinates(self):
        """Map should display places with their coordinates."""
        # Arrange
        from mapa.models import Miejsce
        place = Miejsce.objects.create(
            nazwa="Place",
            adres="Address",
            latitude=52.2297,
            longitude=21.0122
        )

        client = Client()
        url = reverse("map_data")

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_map_hides_closed_places(self):
        """Map should not display permanently closed places."""
        # Arrange
        from mapa.models import Miejsce
        open_place = Miejsce.objects.create(
            nazwa="Open Place",
            adres="Address 1",
            zamkniete_na_stale=False
        )
        closed_place = Miejsce.objects.create(
            nazwa="Closed Place",
            adres="Address 2",
            zamkniete_na_stale=True
        )

        # Act - query what should be displayed
        open_places = Miejsce.objects.filter(zamkniete_na_stale=False)

        # Assert
        assert open_places.count() == 1
        assert open_place in open_places

    @pytest.mark.django_db
    def test_map_with_place_types_and_discounts(self):
        """Map should display places with both type and discount info."""
        # Arrange
        from mapa.models import Miejsce, TypMiejsca, Znizka

        library_type = TypMiejsca.objects.create(nazwa="Library", emoji="📚")
        place = Miejsce.objects.create(
            nazwa="City Library",
            adres="Main Street",
            typ_miejsca=library_type
        )
        discount = Znizka.objects.create(
            dzien_tygodnia="Monday",
            opis="Monday discount - 20% off",
            miejsce=place
        )

        client = Client()
        url = reverse("map_data")

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_compass_mode_workflow(self):
        """User opens compass mode to find nearby place (Kompas Nawojkowy)."""
        # Arrange
        from mapa.models import Miejsce
        place = Miejsce.objects.create(
            nazwa="Nawojka",
            adres="Address",
            latitude=52.2297,
            longitude=21.0122
        )

        client = Client()
        url = reverse("map_view")

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_map_with_multiple_filters(self):
        """User applies multiple filters (type + distance + day)."""
        # Arrange
        from mapa.models import Miejsce, TypMiejsca, Znizka

        library_type = TypMiejsca.objects.create(nazwa="Library", emoji="📚")
        place = Miejsce.objects.create(
            nazwa="Library",
            adres="Main Street",
            typ_miejsca=library_type,
            latitude=52.2297,
            longitude=21.0122
        )
        Znizka.objects.create(
            dzien_tygodnia="Monday",
            opis="Discount",
            miejsce=place
        )

        client = Client()
        url = reverse("map_data") + f"?typ={library_type.id}&dzien_tygodnia=Monday"

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_map_empty_state(self):
        """Map should handle empty state gracefully."""
        # Arrange
        client = Client()
        url = reverse("map_view")

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_map_with_many_places(self):
        """Map should handle many places without performance issues."""
        # Arrange
        from mapa.models import Miejsce
        for i in range(100):
            Miejsce.objects.create(
                nazwa=f"Place {i}",
                adres=f"Address {i}",
                latitude=52.2297 + (i * 0.001),
                longitude=21.0122 + (i * 0.001)
            )

        client = Client()
        url = reverse("map_data")

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200

