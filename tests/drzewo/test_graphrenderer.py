"""
Tests for GraphRenderer.
"""
import pytest


class TestGraphRenderer:
    """Tests for GraphRenderer visualization logic."""

    def test_graph_renderer_instantiation(self):
        """GraphRenderer should be instantiable."""
        # Arrange
        from drzewo.rendering import GraphRenderer

        # Act
        renderer = GraphRenderer()

        # Assert
        assert renderer is not None

    @pytest.mark.django_db
    def test_render_layered_graph_returns_graphviz_output(self):
        """render_layered_graph() should return Graphviz format output."""
        # Arrange
        from drzewo.models import TreeNode, Czlonek
        from drzewo.rendering import GraphRenderer
        member = Czlonek.objects.create(rok_chrztu=1960)
        nodes = [TreeNode(member=member, depth=0, layer=0)]
        edges = []
        renderer = GraphRenderer()

        # Act
        result = renderer.render_layered_graph(nodes, edges)

        # Assert
        assert isinstance(result, str)
        assert "digraph" in result.lower() or "graph" in result.lower()

    @pytest.mark.django_db
    def test_render_layered_graph_includes_all_nodes(self):
        """render_layered_graph() should include all nodes in output."""
        # Arrange
        from drzewo.models import TreeNode, Czlonek
        from drzewo.rendering import GraphRenderer
        member1 = Czlonek.objects.create(rok_chrztu=1960)
        member2 = Czlonek.objects.create(rok_chrztu=1985)
        nodes = [
            TreeNode(member=member1, depth=0, layer=0),
            TreeNode(member=member2, depth=1, layer=0)
        ]
        edges = []
        renderer = GraphRenderer()

        # Act
        result = renderer.render_layered_graph(nodes, edges)

        # Assert
        assert str(member1.pk) in result
        assert str(member2.pk) in result

    @pytest.mark.django_db
    def test_render_layered_graph_includes_all_edges(self):
        """render_layered_graph() should include all edges in output."""
        # Arrange
        from drzewo.models import TreeNode, Czlonek
        from drzewo.rendering import GraphRenderer
        parent = Czlonek.objects.create(rok_chrztu=1960)
        child = Czlonek.objects.create(rodzic_1=parent, rok_chrztu=1985)
        nodes = [
            TreeNode(member=parent, depth=0, layer=0),
            TreeNode(member=child, depth=1, layer=0)
        ]
        edges = [{"source": parent.pk, "target": child.pk}]
        renderer = GraphRenderer()

        # Act
        result = renderer.render_layered_graph(nodes, edges)

        # Assert
        edge_repr = f"{parent.pk} -> {child.pk}" or f"{parent.pk} -- {child.pk}"
        assert edge_repr in result or f'"{parent.pk}"' in result and f'"{child.pk}"' in result

    def test_build_d3_nodes_returns_dict_structure(self):
        """build_d3_nodes() should return dictionary with nodes, links, years, childrenDict."""
        # Arrange
        from drzewo.models import TreeNode, Czlonek
        from drzewo.rendering import GraphRenderer
        member = Czlonek(rok_chrztu=1960)
        nodes = [TreeNode(member=member, depth=0, layer=0, year=1960)]
        edges = []
        renderer = GraphRenderer()

        # Act
        result = renderer.build_d3_nodes(nodes, edges)

        # Assert
        assert "nodes" in result
        assert "links" in result
        assert "years" in result
        assert "childrenDict" in result

    def test_build_d3_nodes_includes_node_data(self):
        """build_d3_nodes() should include node data in D3 format."""
        # Arrange
        from drzewo.models import TreeNode, Czlonek
        from drzewo.rendering import GraphRenderer
        member = Czlonek(pk=1, rok_chrztu=1960)
        nodes = [TreeNode(member=member, depth=0, layer=0, year=1960)]
        edges = []
        renderer = GraphRenderer()

        # Act
        result = renderer.build_d3_nodes(nodes, edges)

        # Assert
        assert len(result["nodes"]) == 1
        assert result["nodes"][0]["id"] == 1

    def test_build_d3_nodes_includes_link_data(self):
        """build_d3_nodes() should include link data in D3 format."""
        # Arrange
        from drzewo.models import TreeNode, Czlonek
        from drzewo.rendering import GraphRenderer
        parent = Czlonek(pk=1, rok_chrztu=1960)
        child = Czlonek(pk=2, rok_chrztu=1985)
        nodes = [
            TreeNode(member=parent, depth=0, layer=0),
            TreeNode(member=child, depth=1, layer=0)
        ]
        edges = [{"source": 1, "target": 2}]
        renderer = GraphRenderer()

        # Act
        result = renderer.build_d3_nodes(nodes, edges)

        # Assert
        assert len(result["links"]) == 1
        assert result["links"][0]["source"] == 1
        assert result["links"][0]["target"] == 2

    def test_build_d3_nodes_collects_unique_years(self):
        """build_d3_nodes() should collect unique years from all nodes."""
        # Arrange
        from drzewo.models import TreeNode, Czlonek
        from drzewo.rendering import GraphRenderer
        member1 = Czlonek(rok_chrztu=1960)
        member2 = Czlonek(rok_chrztu=1985)
        member3 = Czlonek(rok_chrztu=1960)  # Duplicate year
        nodes = [
            TreeNode(member=member1, depth=0, layer=0, year=1960),
            TreeNode(member=member2, depth=1, layer=0, year=1985),
            TreeNode(member=member3, depth=1, layer=1, year=1960)
        ]
        edges = []
        renderer = GraphRenderer()

        # Act
        result = renderer.build_d3_nodes(nodes, edges)

        # Assert
        assert "years" in result
        assert len(result["years"]) == 2
        assert 1960 in result["years"]
        assert 1985 in result["years"]

    def test_build_d3_nodes_builds_children_dict(self):
        """build_d3_nodes() should build childrenDict mapping parent to children."""
        # Arrange
        from drzewo.models import TreeNode, Czlonek
        from drzewo.rendering import GraphRenderer
        parent = Czlonek(pk=1, rok_chrztu=1960)
        child1 = Czlonek(pk=2, rok_chrztu=1985)
        child2 = Czlonek(pk=3, rok_chrztu=1987)
        nodes = [
            TreeNode(member=parent, depth=0, layer=0),
            TreeNode(member=child1, depth=1, layer=0),
            TreeNode(member=child2, depth=1, layer=1)
        ]
        edges = [
            {"source": 1, "target": 2},
            {"source": 1, "target": 3}
        ]
        renderer = GraphRenderer()

        # Act
        result = renderer.build_d3_nodes(nodes, edges)

        # Assert
        assert "childrenDict" in result
        assert 1 in result["childrenDict"]
        assert 2 in result["childrenDict"][1]
        assert 3 in result["childrenDict"][1]

    @pytest.mark.django_db
    def test_render_layered_graph_handles_empty_nodes(self):
        """render_layered_graph() should handle empty node list."""
        # Arrange
        from drzewo.rendering import GraphRenderer
        nodes = []
        edges = []
        renderer = GraphRenderer()

        # Act
        result = renderer.render_layered_graph(nodes, edges)

        # Assert
        assert isinstance(result, str)

    def test_build_d3_nodes_handles_empty_nodes(self):
        """build_d3_nodes() should handle empty node list."""
        # Arrange
        from drzewo.rendering import GraphRenderer
        nodes = []
        edges = []
        renderer = GraphRenderer()

        # Act
        result = renderer.build_d3_nodes(nodes, edges)

        # Assert
        assert len(result["nodes"]) == 0
        assert len(result["links"]) == 0

