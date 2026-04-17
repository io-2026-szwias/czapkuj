"""
Tests for TreeService.
"""
import pytest


class TestTreeService:
    """Tests for TreeService tree building logic."""

    def test_tree_service_instantiation(self):
        """TreeService should be instantiable."""
        # Arrange
        from drzewo.services import TreeService

        # Act
        service = TreeService()

        # Assert
        assert service is not None

    @pytest.mark.django_db
    def test_build_layers_and_edges_from_db_returns_structure(self):
        """build_layers_and_edges_from_db() should return layers and edges."""
        # Arrange
        from drzewo.models import Czlonek
        from drzewo.services import TreeService
        grandparent = Czlonek.objects.create(rok_chrztu=1930)
        parent = Czlonek.objects.create(rodzic_1=grandparent, rok_chrztu=1960)
        child = Czlonek.objects.create(rodzic_1=parent, rok_chrztu=1985)
        service = TreeService()

        # Act
        layers, edges = service.build_layers_and_edges_from_db()

        # Assert
        assert isinstance(layers, dict)
        assert isinstance(edges, list)

    @pytest.mark.django_db
    def test_build_layers_and_edges_groups_by_generation(self):
        """build_layers_and_edges_from_db() should group members by generation."""
        # Arrange
        from drzewo.models import Czlonek
        from drzewo.services import TreeService
        grandparent = Czlonek.objects.create(rok_chrztu=1930)
        parent1 = Czlonek.objects.create(rodzic_1=grandparent, rok_chrztu=1960)
        parent2 = Czlonek.objects.create(rodzic_1=grandparent, rok_chrztu=1962)
        child = Czlonek.objects.create(rodzic_1=parent1, rok_chrztu=1985)
        service = TreeService()

        # Act
        layers, edges = service.build_layers_and_edges_from_db()

        # Assert
        assert 0 in layers  # depth 0
        assert grandparent in layers[0]
        assert 1 in layers
        assert parent1 in layers[1]
        assert parent2 in layers[1]
        assert 2 in layers
        assert child in layers[2]

    @pytest.mark.django_db
    def test_build_layers_and_edges_creates_parent_child_edges(self):
        """build_layers_and_edges_from_db() should create edges between parent and child."""
        # Arrange
        from drzewo.models import Czlonek
        from drzewo.services import TreeService
        parent = Czlonek.objects.create(rok_chrztu=1960)
        child = Czlonek.objects.create(rodzic_1=parent, rok_chrztu=1985)
        service = TreeService()

        # Act
        layers, edges = service.build_layers_and_edges_from_db()

        # Assert
        edge_exists = any(e["source"] == parent.pk and e["target"] == child.pk for e in edges)
        assert edge_exists

    @pytest.mark.django_db
    def test_generate_full_tree_returns_treenodes(self):
        """generate_full_tree() should return list of TreeNode objects."""
        # Arrange
        from drzewo.models import Czlonek
        from drzewo.services import TreeService
        member = Czlonek.objects.create(rok_chrztu=1960)
        service = TreeService()

        # Act
        tree = service.generate_full_tree()

        # Assert
        assert isinstance(tree, list)
        assert len(tree) > 0

    @pytest.mark.django_db
    def test_generate_full_tree_assigns_depth_to_nodes(self):
        """generate_full_tree() should assign depth to each node."""
        # Arrange
        from drzewo.models import Czlonek, TreeNode
        from drzewo.services import TreeService
        grandparent = Czlonek.objects.create(rok_chrztu=1930)
        parent = Czlonek.objects.create(rodzic_1=grandparent, rok_chrztu=1960)
        child = Czlonek.objects.create(rodzic_1=parent, rok_chrztu=1985)
        service = TreeService()

        # Act
        tree = service.generate_full_tree()

        # Assert
        depths = [node.depth for node in tree]
        assert 0 in depths
        assert 1 in depths
        assert 2 in depths

    @pytest.mark.django_db
    def test_generate_full_tree_assigns_year_to_nodes(self):
        """generate_full_tree() should assign year to each node."""
        # Arrange
        from drzewo.models import Czlonek
        from drzewo.services import TreeService
        member = Czlonek.objects.create(rok_chrztu=1960)
        service = TreeService()

        # Act
        tree = service.generate_full_tree()

        # Assert
        for node in tree:
            assert node.year is not None
            assert isinstance(node.year, int)

    @pytest.mark.django_db
    def test_generate_full_tree_assigns_layer_to_nodes(self):
        """generate_full_tree() should assign layer (horizontal position) to each node."""
        # Arrange
        from drzewo.models import Czlonek
        from drzewo.services import TreeService
        parent = Czlonek.objects.create(rok_chrztu=1960)
        child1 = Czlonek.objects.create(rodzic_1=parent, rok_chrztu=1985)
        child2 = Czlonek.objects.create(rodzic_1=parent, rok_chrztu=1987)
        service = TreeService()

        # Act
        tree = service.generate_full_tree()

        # Assert
        layers = [node.layer for node in tree]
        assert len(set(layers)) >= 2  # At least 2 different layers for siblings

    @pytest.mark.django_db
    def test_build_layers_and_edges_handles_single_member(self):
        """build_layers_and_edges_from_db() should handle a single member with no parents."""
        # Arrange
        from drzewo.models import Czlonek
        from drzewo.services import TreeService
        root = Czlonek.objects.create(rok_chrztu=1930)
        service = TreeService()

        # Act
        layers, edges = service.build_layers_and_edges_from_db()

        # Assert
        assert 0 in layers
        assert root in layers[0]
        assert len(edges) == 0

    @pytest.mark.django_db
    def test_build_layers_and_edges_handles_multiple_roots(self):
        """build_layers_and_edges_from_db() should handle multiple root members."""
        # Arrange
        from drzewo.models import Czlonek
        from drzewo.services import TreeService
        root1 = Czlonek.objects.create(rok_chrztu=1930)
        root2 = Czlonek.objects.create(rok_chrztu=1935)
        service = TreeService()

        # Act
        layers, edges = service.build_layers_and_edges_from_db()

        # Assert
        assert 0 in layers
        assert root1 in layers[0]
        assert root2 in layers[0]

