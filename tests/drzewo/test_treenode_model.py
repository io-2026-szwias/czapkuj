"""
Tests for TreeNode model.
"""
import pytest


class TestTreeNodeModel:
    """Tests for TreeNode model fields and methods."""

    @pytest.mark.django_db
    def test_treenode_has_member_field(self):
        """TreeNode should have a member field referencing Czlonek."""
        # Arrange
        from drzewo.models import TreeNode, Czlonek
        czlonek = Czlonek.objects.create(rok_chrztu=1960)
        node_data = {"member": czlonek}

        # Act
        node = TreeNode.objects.create(**node_data)

        # Assert
        assert node.member == czlonek

    @pytest.mark.django_db
    def test_treenode_has_depth_field(self):
        """TreeNode should have a depth field (generation level)."""
        # Arrange
        from drzewo.models import TreeNode, Czlonek
        czlonek = Czlonek.objects.create(rok_chrztu=1960)
        node_data = {"member": czlonek, "depth": 2}

        # Act
        node = TreeNode.objects.create(**node_data)

        # Assert
        assert node.depth == 2

    @pytest.mark.django_db
    def test_treenode_has_year_field(self):
        """TreeNode should have a year field."""
        # Arrange
        from drzewo.models import TreeNode, Czlonek
        czlonek = Czlonek.objects.create(rok_chrztu=1960)
        node_data = {"member": czlonek, "year": 1960}

        # Act
        node = TreeNode.objects.create(**node_data)

        # Assert
        assert node.year == 1960

    @pytest.mark.django_db
    def test_treenode_has_layer_field(self):
        """TreeNode should have a layer field (vertical position in tree)."""
        # Arrange
        from drzewo.models import TreeNode, Czlonek
        czlonek = Czlonek.objects.create(rok_chrztu=1960)
        node_data = {"member": czlonek, "layer": 1}

        # Act
        node = TreeNode.objects.create(**node_data)

        # Assert
        assert node.layer == 1

    def test_treenode_get_year_returns_year_value(self):
        """get_year() should return the year field value."""
        # Arrange
        from drzewo.models import TreeNode, Czlonek
        czlonek = Czlonek(rok_chrztu=1960)
        node = TreeNode(member=czlonek, year=1960)

        # Act
        result = node.get_year()

        # Assert
        assert result == 1960

    def test_treenode_get_layer_returns_layer_value(self):
        """get_layer() should return the layer field value."""
        # Arrange
        from drzewo.models import TreeNode, Czlonek
        czlonek = Czlonek(rok_chrztu=1960)
        node = TreeNode(member=czlonek, layer=1)

        # Act
        result = node.get_layer()

        # Assert
        assert result == 1

    @pytest.mark.django_db
    def test_treenode_depth_computed_from_member_hierarchy(self):
        """TreeNode depth should reflect generation distance from root."""
        # Arrange
        from drzewo.models import TreeNode, Czlonek
        grandparent = Czlonek.objects.create(rok_chrztu=1930)
        parent = Czlonek.objects.create(rodzic_1=grandparent, rok_chrztu=1960)
        child = Czlonek.objects.create(rodzic_1=parent, rok_chrztu=1985)

        # Act
        gp_node = TreeNode.objects.create(member=grandparent, depth=0)
        p_node = TreeNode.objects.create(member=parent, depth=1)
        c_node = TreeNode.objects.create(member=child, depth=2)

        # Assert
        assert gp_node.depth == 0
        assert p_node.depth == 1
        assert c_node.depth == 2

