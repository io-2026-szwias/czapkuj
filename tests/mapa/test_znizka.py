"""
Tests for Znizka (Discount) model.
"""
import pytest
from datetime import date


class TestZnizka:
    """Tests for Discount model."""

    @pytest.mark.django_db
    def test_znizka_has_dzien_tygodnia_field(self):
        """Znizka should have dzien_tygodnia (day of week) field."""
        # Arrange
        from mapa.models import Znizka

        # Act
        discount = Znizka.objects.create(
            dzien_tygodnia="Monday",
            opis="Monday discount"
        )

        # Assert
        assert discount.dzien_tygodnia == "Monday"

    @pytest.mark.django_db
    def test_znizka_has_opis_field(self):
        """Znizka should have opis (description) field."""
        # Arrange
        from mapa.models import Znizka

        # Act
        discount = Znizka.objects.create(
            dzien_tygodnia="Tuesday",
            opis="Tuesday special offer - 20% off"
        )

        # Assert
        assert discount.opis == "Tuesday special offer - 20% off"

    @pytest.mark.django_db
    def test_znizka_related_to_miejsce(self):
        """Znizka should be related to Miejsce."""
        # Arrange
        from mapa.models import Znizka, Miejsce
        place = Miejsce.objects.create(nazwa="Place", adres="Address")

        # Act
        discount = Znizka.objects.create(
            dzien_tygodnia="Monday",
            opis="Monday discount",
            miejsce=place
        )

        # Assert
        assert discount.miejsce == place

    @pytest.mark.django_db
    def test_create_multiple_discounts(self):
        """Should be able to create multiple discounts."""
        # Arrange
        from mapa.models import Znizka, Miejsce
        place = Miejsce.objects.create(nazwa="Place", adres="Address")

        # Act
        discount1 = Znizka.objects.create(
            dzien_tygodnia="Monday",
            opis="Monday discount",
            miejsce=place
        )
        discount2 = Znizka.objects.create(
            dzien_tygodnia="Friday",
            opis="Friday discount",
            miejsce=place
        )

        # Assert
        assert Znizka.objects.count() == 2

    @pytest.mark.django_db
    def test_query_discounts_by_day(self):
        """Should be able to query discounts by day of week."""
        # Arrange
        from mapa.models import Znizka, Miejsce
        place1 = Miejsce.objects.create(nazwa="Place 1", adres="Address 1")
        place2 = Miejsce.objects.create(nazwa="Place 2", adres="Address 2")

        Znizka.objects.create(dzien_tygodnia="Monday", opis="Monday 1", miejsce=place1)
        Znizka.objects.create(dzien_tygodnia="Tuesday", opis="Tuesday", miejsce=place1)
        Znizka.objects.create(dzien_tygodnia="Monday", opis="Monday 2", miejsce=place2)

        # Act
        monday_discounts = Znizka.objects.filter(dzien_tygodnia="Monday")

        # Assert
        assert monday_discounts.count() == 2

    @pytest.mark.django_db
    def test_query_discounts_for_place(self):
        """Should be able to query all discounts for a specific place."""
        # Arrange
        from mapa.models import Znizka, Miejsce
        place1 = Miejsce.objects.create(nazwa="Place 1", adres="Address 1")
        place2 = Miejsce.objects.create(nazwa="Place 2", adres="Address 2")

        Znizka.objects.create(dzien_tygodnia="Monday", opis="Discount 1", miejsce=place1)
        Znizka.objects.create(dzien_tygodnia="Tuesday", opis="Discount 2", miejsce=place1)
        Znizka.objects.create(dzien_tygodnia="Monday", opis="Discount 3", miejsce=place2)

        # Act
        place1_discounts = Znizka.objects.filter(miejsce=place1)

        # Assert
        assert place1_discounts.count() == 2

    @pytest.mark.django_db
    def test_multiple_discounts_same_place_same_day(self):
        """Multiple discounts can exist for same place on same day."""
        # Arrange
        from mapa.models import Znizka, Miejsce
        place = Miejsce.objects.create(nazwa="Place", adres="Address")

        # Act
        discount1 = Znizka.objects.create(
            dzien_tygodnia="Monday",
            opis="Discount 1",
            miejsce=place
        )
        discount2 = Znizka.objects.create(
            dzien_tygodnia="Monday",
            opis="Discount 2",
            miejsce=place
        )

        # Assert
        monday_discounts = Znizka.objects.filter(dzien_tygodnia="Monday", miejsce=place)
        assert monday_discounts.count() == 2

    @pytest.mark.django_db
    def test_query_discounts_by_day_and_place(self):
        """Should be able to query discounts by both day and place."""
        # Arrange
        from mapa.models import Znizka, Miejsce
        place1 = Miejsce.objects.create(nazwa="Place 1", adres="Address 1")
        place2 = Miejsce.objects.create(nazwa="Place 2", adres="Address 2")

        Znizka.objects.create(dzien_tygodnia="Monday", opis="Discount 1", miejsce=place1)
        Znizka.objects.create(dzien_tygodnia="Tuesday", opis="Discount 2", miejsce=place1)
        Znizka.objects.create(dzien_tygodnia="Monday", opis="Discount 3", miejsce=place2)

        # Act
        result = Znizka.objects.filter(dzien_tygodnia="Monday", miejsce=place1)

        # Assert
        assert result.count() == 1
        assert result.first().opis == "Discount 1"

