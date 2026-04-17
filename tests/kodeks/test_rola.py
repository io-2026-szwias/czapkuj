"""
Tests for Rola (Role) model.
"""
import pytest


class TestRola:
    """Tests for Role model (inherits from Podmiot)."""

    @pytest.mark.django_db
    def test_rola_inherits_from_podmiot(self):
        """Rola should inherit from Podmiot."""
        # Arrange
        from kodeks.models import Rola
        
        # Act
        role = Rola.objects.create(
            nazwa="President",
            opis="Presidential role"
        )

        # Assert
        assert role.nazwa == "President"
        assert role.opis == "Presidential role"
        assert role.aktualne is True

    @pytest.mark.django_db
    def test_rola_has_inherited_aktualne_field(self):
        """Rola should have inherited aktualne field."""
        # Arrange
        from kodeks.models import Rola
        
        # Act
        role = Rola.objects.create(
            nazwa="Role",
            aktualne=False
        )

        # Assert
        assert role.aktualne is False

    @pytest.mark.django_db
    def test_create_multiple_roles(self):
        """Should be able to create multiple roles."""
        # Arrange
        from kodeks.models import Rola
        
        # Act
        role1 = Rola.objects.create(nazwa="President")
        role2 = Rola.objects.create(nazwa="Vice President")

        # Assert
        assert Rola.objects.count() == 2

    @pytest.mark.django_db
    def test_query_active_roles(self):
        """Should be able to query active roles."""
        # Arrange
        from kodeks.models import Rola
        Rola.objects.create(nazwa="Active Role", aktualne=True)
        Rola.objects.create(nazwa="Inactive Role", aktualne=False)

        # Act
        active_roles = Rola.objects.filter(aktualne=True)

        # Assert
        assert active_roles.count() == 1
        assert active_roles.first().nazwa == "Active Role"

    @pytest.mark.django_db
    def test_query_inactive_roles(self):
        """Should be able to query inactive roles."""
        # Arrange
        from kodeks.models import Rola
        Rola.objects.create(nazwa="Active Role", aktualne=True)
        Rola.objects.create(nazwa="Inactive Role", aktualne=False)

        # Act
        inactive_roles = Rola.objects.filter(aktualne=False)

        # Assert
        assert inactive_roles.count() == 1
        assert inactive_roles.first().nazwa == "Inactive Role"

    @pytest.mark.django_db
    def test_role_with_description(self):
        """Role can have detailed description."""
        # Arrange
        from kodeks.models import Rola
        
        # Act
        role = Rola.objects.create(
            nazwa="Treasurer",
            opis="Responsible for finances and budget management"
        )

        # Assert
        assert role.opis == "Responsible for finances and budget management"

    @pytest.mark.django_db
    def test_role_without_description(self):
        """Role description can be optional."""
        # Arrange
        from kodeks.models import Rola
        
        # Act
        role = Rola.objects.create(
            nazwa="Secretary",
            opis=None
        )

        # Assert
        assert role.opis is None

