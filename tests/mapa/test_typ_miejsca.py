"""
Tests for TypMiejsca (Place Type) model.
"""
import pytest


class TestTypMiejsca:
    """Tests for Place Type model."""

    @pytest.mark.django_db
    def test_typ_miejsca_has_nazwa_field(self):
        """TypMiejsca should have nazwa (name) field."""
        # Arrange
        from mapa.models import TypMiejsca

        # Act
        place_type = TypMiejsca.objects.create(
            nazwa="Library",
            emoji="📚"
        )

        # Assert
        assert place_type.nazwa == "Library"

    @pytest.mark.django_db
    def test_typ_miejsca_has_emoji_field(self):
        """TypMiejsca should have emoji field."""
        # Arrange
        from mapa.models import TypMiejsca

        # Act
        place_type = TypMiejsca.objects.create(
            nazwa="Park",
            emoji="🌳"
        )

        # Assert
        assert place_type.emoji == "🌳"

    @pytest.mark.django_db
    def test_create_multiple_place_types(self):
        """Should be able to create multiple place types."""
        # Arrange
        from mapa.models import TypMiejsca

        # Act
        type1 = TypMiejsca.objects.create(nazwa="Library", emoji="📚")
        type2 = TypMiejsca.objects.create(nazwa="Park", emoji="🌳")

        # Assert
        assert TypMiejsca.objects.count() == 2

    @pytest.mark.django_db
    def test_query_place_type_by_name(self):
        """Should be able to query place type by name."""
        # Arrange
        from mapa.models import TypMiejsca
        TypMiejsca.objects.create(nazwa="Library", emoji="📚")
        TypMiejsca.objects.create(nazwa="Park", emoji="🌳")

        # Act
        library_type = TypMiejsca.objects.filter(nazwa="Library").first()

        # Assert
        assert library_type.emoji == "📚"

    @pytest.mark.django_db
    def test_multiple_places_can_have_same_type(self):
        """Multiple places can have the same type."""
        # Arrange
        from mapa.models import TypMiejsca, Miejsce
        place_type = TypMiejsca.objects.create(nazwa="Library", emoji="📚")

        # Act
        place1 = Miejsce.objects.create(
            nazwa="City Library",
            adres="Main Street",
            typ_miejsca=place_type
        )
        place2 = Miejsce.objects.create(
            nazwa="Central Library",
            adres="Central Avenue",
            typ_miejsca=place_type
        )

        # Assert
        places_with_type = Miejsce.objects.filter(typ_miejsca=place_type)
        assert places_with_type.count() == 2

    @pytest.mark.django_db
    def test_query_places_by_type(self):
        """Should be able to query all places of a specific type."""
        # Arrange
        from mapa.models import TypMiejsca, Miejsce
        library_type = TypMiejsca.objects.create(nazwa="Library", emoji="📚")
        park_type = TypMiejsca.objects.create(nazwa="Park", emoji="🌳")

        Miejsce.objects.create(nazwa="City Library", adres="Address 1", typ_miejsca=library_type)
        Miejsce.objects.create(nazwa="Central Library", adres="Address 2", typ_miejsca=library_type)
        Miejsce.objects.create(nazwa="Central Park", adres="Address 3", typ_miejsca=park_type)

        # Act
        libraries = Miejsce.objects.filter(typ_miejsca=library_type)
        parks = Miejsce.objects.filter(typ_miejsca=park_type)

        # Assert
        assert libraries.count() == 2
        assert parks.count() == 1

