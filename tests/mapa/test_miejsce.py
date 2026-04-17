"""
Tests for Miejsce (Place) model.
"""
import pytest


class TestMiejsce:
    """Tests for Place model."""

    @pytest.mark.django_db
    def test_miejsce_has_nazwa_field(self):
        """Miejsce should have nazwa (name) field."""
        # Arrange
        from mapa.models import Miejsce

        # Act
        place = Miejsce.objects.create(
            nazwa="Library",
            adres="Main Street 1"
        )

        # Assert
        assert place.nazwa == "Library"

    @pytest.mark.django_db
    def test_miejsce_has_adres_field(self):
        """Miejsce should have adres (address) field."""
        # Arrange
        from mapa.models import Miejsce

        # Act
        place = Miejsce.objects.create(
            nazwa="Place",
            adres="123 Main Street"
        )

        # Assert
        assert place.adres == "123 Main Street"

    @pytest.mark.django_db
    def test_miejsce_has_latitude_field(self):
        """Miejsce should have latitude field."""
        # Arrange
        from mapa.models import Miejsce

        # Act
        place = Miejsce.objects.create(
            nazwa="Place",
            adres="Address",
            latitude=52.2297,
            longitude=21.0122
        )

        # Assert
        assert place.latitude == 52.2297

    @pytest.mark.django_db
    def test_miejsce_has_longitude_field(self):
        """Miejsce should have longitude field."""
        # Arrange
        from mapa.models import Miejsce

        # Act
        place = Miejsce.objects.create(
            nazwa="Place",
            adres="Address",
            latitude=52.2297,
            longitude=21.0122
        )

        # Assert
        assert place.longitude == 21.0122

    @pytest.mark.django_db
    def test_miejsce_has_zamkniete_na_stale_field(self):
        """Miejsce should have zamkniete_na_stale (permanently closed) field."""
        # Arrange
        from mapa.models import Miejsce

        # Act
        place = Miejsce.objects.create(
            nazwa="Place",
            adres="Address",
            zamkniete_na_stale=False
        )

        # Assert
        assert place.zamkniete_na_stale is False

    @pytest.mark.django_db
    def test_miejsce_can_be_marked_closed(self):
        """Miejsce can be marked as permanently closed."""
        # Arrange
        from mapa.models import Miejsce

        # Act
        place = Miejsce.objects.create(
            nazwa="Closed Place",
            adres="Address",
            zamkniete_na_stale=True
        )

        # Assert
        assert place.zamkniete_na_stale is True

    @pytest.mark.django_db
    def test_query_open_places(self):
        """Should be able to query open places."""
        # Arrange
        from mapa.models import Miejsce
        Miejsce.objects.create(nazwa="Open 1", adres="Address 1", zamkniete_na_stale=False)
        Miejsce.objects.create(nazwa="Closed", adres="Address 2", zamkniete_na_stale=True)
        Miejsce.objects.create(nazwa="Open 2", adres="Address 3", zamkniete_na_stale=False)

        # Act
        open_places = Miejsce.objects.filter(zamkniete_na_stale=False)

        # Assert
        assert open_places.count() == 2

    @pytest.mark.django_db
    def test_query_closed_places(self):
        """Should be able to query closed places."""
        # Arrange
        from mapa.models import Miejsce
        Miejsce.objects.create(nazwa="Open", adres="Address 1", zamkniete_na_stale=False)
        Miejsce.objects.create(nazwa="Closed 1", adres="Address 2", zamkniete_na_stale=True)
        Miejsce.objects.create(nazwa="Closed 2", adres="Address 3", zamkniete_na_stale=True)

        # Act
        closed_places = Miejsce.objects.filter(zamkniete_na_stale=True)

        # Assert
        assert closed_places.count() == 2

    @pytest.mark.django_db
    def test_miejsce_has_type_relationship(self):
        """Miejsce should be related to TypMiejsca."""
        # Arrange
        from mapa.models import Miejsce, TypMiejsca
        place_type = TypMiejsca.objects.create(nazwa="Library", emoji="📚")

        # Act
        place = Miejsce.objects.create(
            nazwa="City Library",
            adres="Main Street",
            typ_miejsca=place_type
        )

        # Assert
        assert place.typ_miejsca == place_type

    @pytest.mark.django_db
    def test_create_multiple_places(self):
        """Should be able to create multiple places."""
        # Arrange
        from mapa.models import Miejsce

        # Act
        place1 = Miejsce.objects.create(nazwa="Place 1", adres="Address 1")
        place2 = Miejsce.objects.create(nazwa="Place 2", adres="Address 2")

        # Assert
        assert Miejsce.objects.count() == 2

    @pytest.mark.django_db
    def test_latitude_longitude_optional(self):
        """Latitude and longitude should be optional."""
        # Arrange
        from mapa.models import Miejsce

        # Act
        place = Miejsce.objects.create(
            nazwa="Place",
            adres="Address",
            latitude=None,
            longitude=None
        )

        # Assert
        assert place.latitude is None
        assert place.longitude is None

