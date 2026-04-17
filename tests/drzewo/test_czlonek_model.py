"""
Tests for Czlonek (Member) model.
"""
import pytest


class TestCzlonekModel:
    """Tests for Czlonek model fields and relationships."""

    @pytest.mark.django_db
    def test_czlonek_has_primary_key(self):
        """Czlonek instance should have a primary key after saving."""
        # Arrange
        from drzewo.models import Czlonek
        czlonek = Czlonek.objects.create(rok_chrztu=1960)

        # Act & Assert
        assert czlonek.pk is not None

    @pytest.mark.django_db
    def test_czlonek_rok_chrztu_field_exists(self):
        """Czlonek should have rok_chrztu (baptism year) field."""
        # Arrange
        from drzewo.models import Czlonek
        czlonek_data = {"rok_chrztu": 1990}

        # Act
        czlonek = Czlonek.objects.create(**czlonek_data)

        # Assert
        assert czlonek.rok_chrztu == 1990

    @pytest.mark.django_db
    def test_czlonek_staz_field_exists(self):
        """Czlonek should have staz (tenure) field."""
        # Arrange
        from drzewo.models import Czlonek
        czlonek_data = {"staz": 5}

        # Act
        czlonek = Czlonek.objects.create(**czlonek_data)

        # Assert
        assert czlonek.staz == 5

    @pytest.mark.django_db
    def test_czlonek_has_parent_relationships(self):
        """Czlonek should have rodzic_1 and rodzic_2 relationships."""
        # Arrange
        from drzewo.models import Czlonek
        parent1 = Czlonek.objects.create(rok_chrztu=1960)
        parent2 = Czlonek.objects.create(rok_chrztu=1965)
        child = Czlonek(rodzic_1=parent1, rodzic_2=parent2)

        # Act
        child.save()

        # Assert
        assert child.rodzic_1 == parent1
        assert child.rodzic_2 == parent2

    @pytest.mark.django_db
    def test_czlonek_parent_1_field_nullable(self):
        """rodzic_1 field should be nullable (member may not have parent1 info)."""
        # Arrange
        from drzewo.models import Czlonek
        czlonek_data = {"rodzic_1": None}

        # Act
        czlonek = Czlonek.objects.create(**czlonek_data)

        # Assert
        assert czlonek.rodzic_1 is None

    @pytest.mark.django_db
    def test_czlonek_parent_2_field_nullable(self):
        """rodzic_2 field should be nullable (member may not have parent2 info)."""
        # Arrange
        from drzewo.models import Czlonek
        czlonek_data = {"rodzic_2": None}

        # Act
        czlonek = Czlonek.objects.create(**czlonek_data)

        # Assert
        assert czlonek.rodzic_2 is None

    @pytest.mark.django_db
    def test_get_member_children_returns_direct_children(self):
        """get_member_children() should return members where this member is parent1 or parent2."""
        # Arrange
        from drzewo.models import Czlonek
        parent = Czlonek.objects.create(rok_chrztu=1960)
        child1 = Czlonek.objects.create(rodzic_1=parent, rok_chrztu=1985)
        child2 = Czlonek.objects.create(rodzic_2=parent, rok_chrztu=1987)
        unrelated = Czlonek.objects.create(rok_chrztu=1990)

        # Act
        children = parent.get_member_children()

        # Assert
        assert child1 in children
        assert child2 in children
        assert unrelated not in children
        assert len(children) == 2

    @pytest.mark.django_db
    def test_get_member_children_empty_for_childless_member(self):
        """get_member_children() should return empty list for members without children."""
        # Arrange
        from drzewo.models import Czlonek
        parent = Czlonek.objects.create(rok_chrztu=1960)

        # Act
        children = parent.get_member_children()

        # Assert
        assert len(children) == 0

    @pytest.mark.django_db
    def test_get_member_step_children_returns_step_children(self):
        """get_member_step_children() should return children of spouse's partner."""
        # Arrange
        from drzewo.models import Czlonek
        grandparent1 = Czlonek.objects.create(rok_chrztu=1935)
        grandparent2 = Czlonek.objects.create(rok_chrztu=1940)
        parent1 = Czlonek.objects.create(rodzic_1=grandparent1, rok_chrztu=1960)
        parent2 = Czlonek.objects.create(rodzic_1=grandparent2, rok_chrztu=1962)
        step_child = Czlonek.objects.create(rodzic_1=parent2, rok_chrztu=1985)

        # Act
        step_children = parent1.get_member_step_children()

        # Assert
        assert step_child in step_children

    @pytest.mark.django_db
    def test_get_member_step_children_empty_for_no_spouse(self):
        """get_member_step_children() should return empty list if member has no spouse."""
        # Arrange
        from drzewo.models import Czlonek
        member = Czlonek.objects.create(rok_chrztu=1960)

        # Act
        step_children = member.get_member_step_children()

        # Assert
        assert len(step_children) == 0

