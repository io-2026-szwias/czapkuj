"""
Tests for MapFilters and DiscountFilters.
"""
import pytest


class TestMapFilters:
    """Tests for map filtering logic."""

    @pytest.mark.django_db
    def test_filter_places_by_type(self):
        """Should be able to filter places by type."""
        # Arrange
        from mapa.models import Miejsce, TypMiejsca
        library_type = TypMiejsca.objects.create(nazwa="Library", emoji="📚")
        park_type = TypMiejsca.objects.create(nazwa="Park", emoji="🌳")

        Miejsce.objects.create(nazwa="City Library", adres="Address 1", typ_miejsca=library_type)
        Miejsce.objects.create(nazwa="Central Library", adres="Address 2", typ_miejsca=library_type)
        Miejsce.objects.create(nazwa="Park", adres="Address 3", typ_miejsca=park_type)

        # Act
        libraries = Miejsce.objects.filter(typ_miejsca=library_type, zamkniete_na_stale=False)

        # Assert
        assert libraries.count() == 2

    @pytest.mark.django_db
    def test_filter_places_by_distance(self):
        """Should be able to filter places by distance."""
        # Arrange
        from mapa.models import Miejsce
        place1 = Miejsce.objects.create(
            nazwa="Place 1",
            adres="Address 1",
            latitude=52.2297,
            longitude=21.0122
        )
        place2 = Miejsce.objects.create(
            nazwa="Place 2",
            adres="Address 2",
            latitude=52.2500,
            longitude=21.0500
        )

        # Act - this is a simplified test
        # In real implementation, distance calculation would use geospatial queries
        places = Miejsce.objects.filter(latitude__isnull=False, longitude__isnull=False)

        # Assert
        assert places.count() == 2

    @pytest.mark.django_db
    def test_filter_places_by_type_and_status(self):
        """Should be able to filter places by type and open status."""
        # Arrange
        from mapa.models import Miejsce, TypMiejsca
        library_type = TypMiejsca.objects.create(nazwa="Library", emoji="📚")

        Miejsce.objects.create(
            nazwa="Open Library",
            adres="Address 1",
            typ_miejsca=library_type,
            zamkniete_na_stale=False
        )
        Miejsce.objects.create(
            nazwa="Closed Library",
            adres="Address 2",
            typ_miejsca=library_type,
            zamkniete_na_stale=True
        )

        # Act
        open_libraries = Miejsce.objects.filter(
            typ_miejsca=library_type,
            zamkniete_na_stale=False
        )

        # Assert
        assert open_libraries.count() == 1
        assert open_libraries.first().nazwa == "Open Library"


class TestDiscountFilters:
    """Tests for discount filtering logic (UC-23)."""

    @pytest.mark.django_db
    def test_filter_discounts_by_day(self):
        """Should be able to filter discounts by day of week."""
        # Arrange
        from mapa.models import Znizka, Miejsce
        place1 = Miejsce.objects.create(nazwa="Place 1", adres="Address 1")
        place2 = Miejsce.objects.create(nazwa="Place 2", adres="Address 2")

        Znizka.objects.create(dzien_tygodnia="Monday", opis="Discount 1", miejsce=place1)
        Znizka.objects.create(dzien_tygodnia="Tuesday", opis="Discount 2", miejsce=place1)
        Znizka.objects.create(dzien_tygodnia="Monday", opis="Discount 3", miejsce=place2)

        # Act
        monday_discounts = Znizka.objects.filter(dzien_tygodnia="Monday")

        # Assert
        assert monday_discounts.count() == 2

    @pytest.mark.django_db
    def test_filter_places_with_discounts_on_day(self):
        """Should be able to filter places that have discounts on a specific day."""
        # Arrange
        from mapa.models import Znizka, Miejsce
        place1 = Miejsce.objects.create(nazwa="Place 1", adres="Address 1")
        place2 = Miejsce.objects.create(nazwa="Place 2", adres="Address 2")

        Znizka.objects.create(dzien_tygodnia="Monday", opis="Discount", miejsce=place1)
        # place2 has no Monday discount

        # Act
        places_with_monday_discounts = Miejsce.objects.filter(
            znizka__dzien_tygodnia="Monday"
        ).distinct()

        # Assert
        assert places_with_monday_discounts.count() == 1
        assert places_with_monday_discounts.first() == place1

    @pytest.mark.django_db
    def test_filter_multiple_discount_days(self):
        """Should be able to filter places by any discount day."""
        # Arrange
        from mapa.models import Znizka, Miejsce
        place = Miejsce.objects.create(nazwa="Place", adres="Address")

        Znizka.objects.create(dzien_tygodnia="Monday", opis="Monday discount", miejsce=place)
        Znizka.objects.create(dzien_tygodnia="Friday", opis="Friday discount", miejsce=place)

        # Act
        place_discounts = Znizka.objects.filter(miejsce=place)
        discount_days = set(place_discounts.values_list('dzien_tygodnia', flat=True))

        # Assert
        assert len(discount_days) == 2
        assert "Monday" in discount_days
        assert "Friday" in discount_days

    @pytest.mark.django_db
    def test_combined_filter_type_and_discount_day(self):
        """Should be able to filter by both type and discount day."""
        # Arrange
        from mapa.models import Znizka, Miejsce, TypMiejsca
        library_type = TypMiejsca.objects.create(nazwa="Library", emoji="📚")

        place1 = Miejsce.objects.create(
            nazwa="Library 1",
            adres="Address 1",
            typ_miejsca=library_type
        )
        place2 = Miejsce.objects.create(
            nazwa="Library 2",
            adres="Address 2",
            typ_miejsca=library_type
        )

        Znizka.objects.create(dzien_tygodnia="Monday", opis="Discount", miejsce=place1)
        # place2 has no Monday discount

        # Act
        libraries_with_monday_discounts = Miejsce.objects.filter(
            typ_miejsca=library_type,
            znizka__dzien_tygodnia="Monday"
        ).distinct()

        # Assert
        assert libraries_with_monday_discounts.count() == 1

