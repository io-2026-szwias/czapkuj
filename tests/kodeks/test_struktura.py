"""
Tests for Struktura (Structure) model.
"""
import pytest


class TestStruktura:
    """Tests for Structure model (inherits from Podmiot)."""

    @pytest.mark.django_db
    def test_struktura_inherits_from_podmiot(self):
        """Struktura should inherit from Podmiot."""
        # Arrange
        from kodeks.models import Struktura
        
        # Act
        structure = Struktura.objects.create(
            nazwa="Board",
            opis="Board of Directors"
        )

        # Assert
        assert structure.nazwa == "Board"
        assert structure.opis == "Board of Directors"
        assert structure.aktualne is True

    @pytest.mark.django_db
    def test_struktura_has_inherited_aktualne_field(self):
        """Struktura should have inherited aktualne field."""
        # Arrange
        from kodeks.models import Struktura
        
        # Act
        structure = Struktura.objects.create(
            nazwa="Structure",
            aktualne=False
        )

        # Assert
        assert structure.aktualne is False

    @pytest.mark.django_db
    def test_create_multiple_structures(self):
        """Should be able to create multiple structures."""
        # Arrange
        from kodeks.models import Struktura
        
        # Act
        struct1 = Struktura.objects.create(nazwa="Board")
        struct2 = Struktura.objects.create(nazwa="Committee")

        # Assert
        assert Struktura.objects.count() == 2

    @pytest.mark.django_db
    def test_query_active_structures(self):
        """Should be able to query active structures."""
        # Arrange
        from kodeks.models import Struktura
        Struktura.objects.create(nazwa="Active Structure", aktualne=True)
        Struktura.objects.create(nazwa="Inactive Structure", aktualne=False)

        # Act
        active_structures = Struktura.objects.filter(aktualne=True)

        # Assert
        assert active_structures.count() == 1
        assert active_structures.first().nazwa == "Active Structure"

    @pytest.mark.django_db
    def test_query_inactive_structures(self):
        """Should be able to query inactive structures."""
        # Arrange
        from kodeks.models import Struktura
        Struktura.objects.create(nazwa="Active Structure", aktualne=True)
        Struktura.objects.create(nazwa="Inactive Structure", aktualne=False)

        # Act
        inactive_structures = Struktura.objects.filter(aktualne=False)

        # Assert
        assert inactive_structures.count() == 1
        assert inactive_structures.first().nazwa == "Inactive Structure"

    @pytest.mark.django_db
    def test_structure_with_description(self):
        """Structure can have detailed description."""
        # Arrange
        from kodeks.models import Struktura
        
        # Act
        structure = Struktura.objects.create(
            nazwa="Executive Committee",
            opis="Committee responsible for executive decisions"
        )

        # Assert
        assert structure.opis == "Committee responsible for executive decisions"

    @pytest.mark.django_db
    def test_structure_without_description(self):
        """Structure description can be optional."""
        # Arrange
        from kodeks.models import Struktura
        
        # Act
        structure = Struktura.objects.create(
            nazwa="Council",
            opis=None
        )

        # Assert
        assert structure.opis is None

