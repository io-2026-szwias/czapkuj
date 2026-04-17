"""
Tests for Podmiot (Entity/Subject) model.
"""
import pytest


class TestPodmiot:
    """Tests for base Podmiot model."""

    @pytest.mark.django_db
    def test_podmiot_has_nazwa_field(self):
        """Podmiot should have nazwa (name) field."""
        # Arrange
        from kodeks.models import Podmiot
        
        # Act
        entity = Podmiot.objects.create(
            nazwa="Test Entity",
            opis="Test description"
        )

        # Assert
        assert entity.nazwa == "Test Entity"

    @pytest.mark.django_db
    def test_podmiot_has_opis_field(self):
        """Podmiot should have opis (description) field."""
        # Arrange
        from kodeks.models import Podmiot
        
        # Act
        entity = Podmiot.objects.create(
            nazwa="Entity",
            opis="Detailed description"
        )

        # Assert
        assert entity.opis == "Detailed description"

    @pytest.mark.django_db
    def test_podmiot_has_aktualne_field(self):
        """Podmiot should have aktualne (is_active) field."""
        # Arrange
        from kodeks.models import Podmiot
        
        # Act
        entity = Podmiot.objects.create(
            nazwa="Entity",
            aktualne=True
        )

        # Assert
        assert entity.aktualne is True

    @pytest.mark.django_db
    def test_podmiot_aktualne_defaults_to_true(self):
        """aktualne field should default to True."""
        # Arrange
        from kodeks.models import Podmiot
        
        # Act
        entity = Podmiot.objects.create(
            nazwa="Entity",
            opis="Description"
        )

        # Assert
        assert entity.aktualne is True

    @pytest.mark.django_db
    def test_podmiot_can_be_inactive(self):
        """Podmiot can be marked as inactive."""
        # Arrange
        from kodeks.models import Podmiot
        
        # Act
        entity = Podmiot.objects.create(
            nazwa="Entity",
            aktualne=False
        )

        # Assert
        assert entity.aktualne is False

    @pytest.mark.django_db
    def test_query_active_entities(self):
        """Should be able to query active entities."""
        # Arrange
        from kodeks.models import Podmiot
        Podmiot.objects.create(nazwa="Active 1", aktualne=True)
        Podmiot.objects.create(nazwa="Inactive", aktualne=False)
        Podmiot.objects.create(nazwa="Active 2", aktualne=True)

        # Act
        active = Podmiot.objects.filter(aktualne=True)

        # Assert
        assert active.count() == 2

    @pytest.mark.django_db
    def test_query_inactive_entities(self):
        """Should be able to query inactive entities."""
        # Arrange
        from kodeks.models import Podmiot
        Podmiot.objects.create(nazwa="Active", aktualne=True)
        Podmiot.objects.create(nazwa="Inactive 1", aktualne=False)
        Podmiot.objects.create(nazwa="Inactive 2", aktualne=False)

        # Act
        inactive = Podmiot.objects.filter(aktualne=False)

        # Assert
        assert inactive.count() == 2

    @pytest.mark.django_db
    def test_create_multiple_entities(self):
        """Should be able to create multiple entities."""
        # Arrange
        from kodeks.models import Podmiot
        
        # Act
        entity1 = Podmiot.objects.create(nazwa="Entity 1")
        entity2 = Podmiot.objects.create(nazwa="Entity 2")

        # Assert
        assert Podmiot.objects.count() == 2
        assert entity1.nazwa == "Entity 1"
        assert entity2.nazwa == "Entity 2"

    @pytest.mark.django_db
    def test_opis_field_is_optional(self):
        """opis field should be optional."""
        # Arrange
        from kodeks.models import Podmiot
        
        # Act
        entity = Podmiot.objects.create(
            nazwa="Entity",
            opis=None
        )

        # Assert
        assert entity.opis is None

