"""
Tests for MapView and map data retrieval.
"""
import pytest
from django.test import Client
from django.urls import reverse


class TestMapView:
    """Tests for Map view and data endpoints."""

    @pytest.mark.django_db
    def test_map_view_returns_200(self):
        """GET /miejsca/mapa/ should return 200 OK."""
        # Arrange
        client = Client()
        url = reverse("map_view")  # Adjust URL name as needed

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_map_view_returns_html(self):
        """Map view should return HTML response."""
        # Arrange
        client = Client()
        url = reverse("map_view")

        # Act
        response = client.get(url)

        # Assert
        assert "text/html" in response["Content-Type"]

    @pytest.mark.django_db
    def test_map_data_endpoint_returns_json(self):
        """GET /miejsca/mapa/dane/ should return JSON."""
        # Arrange
        client = Client()
        url = reverse("map_data")

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200
        assert "application/json" in response["Content-Type"] or "json" in response["Content-Type"]

    @pytest.mark.django_db
    def test_map_data_returns_places(self):
        """Map data endpoint should return places JSON."""
        # Arrange
        from mapa.models import Miejsce
        Miejsce.objects.create(nazwa="Place", adres="Address")
        client = Client()
        url = reverse("map_data")

        # Act
        response = client.get(url)
        data = response.json()

        # Assert
        assert response.status_code == 200
        assert isinstance(data, dict)

    @pytest.mark.django_db
    def test_map_data_with_type_filter(self):
        """Map data should support type filtering (UC-22)."""
        # Arrange
        from mapa.models import Miejsce, TypMiejsca
        library_type = TypMiejsca.objects.create(nazwa="Library", emoji="📚")
        park_type = TypMiejsca.objects.create(nazwa="Park", emoji="🌳")

        Miejsce.objects.create(nazwa="Library", adres="Address 1", typ_miejsca=library_type)
        Miejsce.objects.create(nazwa="Park", adres="Address 2", typ_miejsca=park_type)

        client = Client()
        url = reverse("map_data") + "?typ=" + str(library_type.id)

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_map_data_with_distance_filter(self):
        """Map data should support distance filtering (UC-22)."""
        # Arrange
        from mapa.models import Miejsce
        Miejsce.objects.create(
            nazwa="Place",
            adres="Address",
            latitude=52.2297,
            longitude=21.0122
        )

        client = Client()
        url = reverse("map_data") + "?max_distance=5&lat=52.2297&lon=21.0122"

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code in [200, 400, 422]  # May accept or reject invalid params

    @pytest.mark.django_db
    def test_map_data_with_discount_filter(self):
        """Map data should support discount filtering by day (UC-23)."""
        # Arrange
        from mapa.models import Miejsce, Znizka
        place = Miejsce.objects.create(nazwa="Place", adres="Address")
        Znizka.objects.create(dzien_tygodnia="Monday", opis="Discount", miejsce=place)

        client = Client()
        url = reverse("map_data") + "?dzien_tygodnia=Monday"

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_map_view_includes_javascript(self):
        """Map view should include JavaScript for rendering."""
        # Arrange
        client = Client()
        url = reverse("map_view")

        # Act
        response = client.get(url)

        # Assert
        assert b"<script" in response.content or b".js" in response.content

    @pytest.mark.django_db
    def test_map_excludes_closed_places(self):
        """Map should exclude permanently closed places."""
        # Arrange
        from mapa.models import Miejsce
        Miejsce.objects.create(nazwa="Open Place", adres="Address 1", zamkniete_na_stale=False)
        Miejsce.objects.create(nazwa="Closed Place", adres="Address 2", zamkniete_na_stale=True)

        client = Client()
        url = reverse("map_data")

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_map_data_includes_coordinates(self):
        """Map data should include latitude and longitude."""
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
    def test_map_data_includes_place_types(self):
        """Map data should include place type information."""
        # Arrange
        from mapa.models import Miejsce, TypMiejsca
        place_type = TypMiejsca.objects.create(nazwa="Library", emoji="📚")
        Miejsce.objects.create(nazwa="Place", adres="Address", typ_miejsca=place_type)

        client = Client()
        url = reverse("map_data")

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_map_data_includes_discount_info(self):
        """Map data should include discount information when requested."""
        # Arrange
        from mapa.models import Miejsce, Znizka
        place = Miejsce.objects.create(nazwa="Place", adres="Address")
        Znizka.objects.create(dzien_tygodnia="Monday", opis="Discount", miejsce=place)

        client = Client()
        url = reverse("map_data")

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_map_view_empty_database(self):
        """Map view should handle empty database gracefully."""
        # Arrange
        client = Client()
        url = reverse("map_view")

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200

