"""
Integration tests for tree building and rendering workflow.
"""
import pytest
from django.test import Client
from django.urls import reverse


class TestTreeBuildingIntegration:
    """Integration tests for complete tree building workflow."""

    @pytest.mark.django_db
    def test_complete_workflow_single_member(self):
        """Should build complete tree with single member."""
        # Arrange
        from drzewo.models import Czlonek
        from drzewo.services import TreeService
        from drzewo.rendering import GraphRenderer
        member = Czlonek.objects.create(rok_chrztu=1960)
        service = TreeService()
        renderer = GraphRenderer()

        # Act
        layers, edges = service.build_layers_and_edges_from_db()
        tree_nodes = service.generate_full_tree()
        d3_data = renderer.build_d3_nodes(tree_nodes, edges)

        # Assert
        assert len(d3_data["nodes"]) == 1
        assert d3_data["nodes"][0]["id"] == member.pk
        assert len(d3_data["links"]) == 0

    @pytest.mark.django_db
    def test_complete_workflow_multi_generation_family(self):
        """Should build complete tree with multiple generations."""
        # Arrange
        from drzewo.models import Czlonek
        from drzewo.services import TreeService
        from drzewo.rendering import GraphRenderer
        grandparent = Czlonek.objects.create(rok_chrztu=1930)
        parent1 = Czlonek.objects.create(rodzic_1=grandparent, rok_chrztu=1960)
        parent2 = Czlonek.objects.create(rodzic_1=grandparent, rok_chrztu=1962)
        child1 = Czlonek.objects.create(rodzic_1=parent1, rok_chrztu=1985)
        child2 = Czlonek.objects.create(rodzic_1=parent2, rok_chrztu=1987)
        service = TreeService()
        renderer = GraphRenderer()

        # Act
        layers, edges = service.build_layers_and_edges_from_db()
        tree_nodes = service.generate_full_tree()
        d3_data = renderer.build_d3_nodes(tree_nodes, edges)

        # Assert
        assert len(d3_data["nodes"]) == 5
        assert len(d3_data["links"]) == 4
        member_ids = [node["id"] for node in d3_data["nodes"]]
        assert grandparent.pk in member_ids
        assert parent1.pk in member_ids
        assert child1.pk in member_ids

    @pytest.mark.django_db
    def test_api_end_to_end_returns_valid_tree_data(self):
        """API endpoint should return valid tree data end-to-end."""
        # Arrange
        from drzewo.models import Czlonek
        parent = Czlonek.objects.create(rok_chrztu=1960)
        child = Czlonek.objects.create(rodzic_1=parent, rok_chrztu=1985)
        client = Client()
        url = reverse("full_tree_data_graphviz")

        # Act
        response = client.get(url)
        data = response.json()

        # Assert
        assert response.status_code == 200
        assert len(data["nodes"]) >= 2
        assert len(data["links"]) >= 1
        node_ids = [n["id"] for n in data["nodes"]]
        assert parent.pk in node_ids
        assert child.pk in node_ids

    @pytest.mark.django_db
    def test_view_and_api_work_together(self):
        """Interactive view and API should work together."""
        # Arrange
        from drzewo.models import Czlonek
        Czlonek.objects.create(rok_chrztu=1960)
        client = Client()
        view_url = reverse("full_tree_interactive_view")
        api_url = reverse("full_tree_data_graphviz")

        # Act
        view_response = client.get(view_url)
        api_response = client.get(api_url)

        # Assert
        assert view_response.status_code == 200
        assert api_response.status_code == 200
        api_data = api_response.json()
        assert len(api_data["nodes"]) > 0

    @pytest.mark.django_db
    def test_layers_computed_correctly_for_deep_tree(self):
        """Layers should be computed correctly for deeply nested families."""
        # Arrange
        from drzewo.models import Czlonek
        from drzewo.services import TreeService
        root = Czlonek.objects.create(rok_chrztu=1900)
        gen1 = Czlonek.objects.create(rodzic_1=root, rok_chrztu=1930)
        gen2 = Czlonek.objects.create(rodzic_1=gen1, rok_chrztu=1960)
        gen3 = Czlonek.objects.create(rodzic_1=gen2, rok_chrztu=1985)
        service = TreeService()

        # Act
        layers, edges = service.build_layers_and_edges_from_db()
        tree_nodes = service.generate_full_tree()

        # Assert
        depths = {node.member.pk: node.depth for node in tree_nodes}
        assert depths[root.pk] == 0
        assert depths[gen1.pk] == 1
        assert depths[gen2.pk] == 2
        assert depths[gen3.pk] == 3

    @pytest.mark.django_db
    def test_siblings_have_different_layers(self):
        """Sibling nodes should have different layers in visualization."""
        # Arrange
        from drzewo.models import Czlonek
        from drzewo.services import TreeService
        from drzewo.rendering import GraphRenderer
        parent = Czlonek.objects.create(rok_chrztu=1960)
        sibling1 = Czlonek.objects.create(rodzic_1=parent, rok_chrztu=1985)
        sibling2 = Czlonek.objects.create(rodzic_1=parent, rok_chrztu=1987)
        sibling3 = Czlonek.objects.create(rodzic_1=parent, rok_chrztu=1990)
        service = TreeService()

        # Act
        tree_nodes = service.generate_full_tree()
        sibling_nodes = [n for n in tree_nodes if n.member.pk in [sibling1.pk, sibling2.pk, sibling3.pk]]
        sibling_layers = [n.layer for n in sibling_nodes]

        # Assert
        assert len(set(sibling_layers)) == 3  # All should have different layers

    @pytest.mark.django_db
    def test_graphviz_output_is_valid_format(self, mocker):
        """Graphviz output should be in valid graph format."""
        # Arrange
        from drzewo.models import Czlonek, TreeNode
        from drzewo.rendering import GraphRenderer
        member = Czlonek.objects.create(rok_chrztu=1960)
        nodes = [TreeNode(member=member, depth=0, layer=0)]
        edges = []
        renderer = GraphRenderer()

        # Act
        result = renderer.render_layered_graph(nodes, edges)

        # Assert
        assert "digraph" in result.lower() or "graph" in result.lower()
        assert "{" in result
        assert "}" in result

    @pytest.mark.django_db
    def test_member_with_both_parents_creates_correct_links(self):
        """Member with both parents should create links to both."""
        # Arrange
        from drzewo.models import Czlonek
        from drzewo.services import TreeService
        parent1 = Czlonek.objects.create(rok_chrztu=1960)
        parent2 = Czlonek.objects.create(rok_chrztu=1962)
        child = Czlonek.objects.create(rodzic_1=parent1, rodzic_2=parent2, rok_chrztu=1985)
        service = TreeService()

        # Act
        layers, edges = service.build_layers_and_edges_from_db()

        # Assert
        parent1_to_child = any(e["source"] == parent1.pk and e["target"] == child.pk for e in edges)
        parent2_to_child = any(e["source"] == parent2.pk and e["target"] == child.pk for e in edges)
        assert parent1_to_child
        assert parent2_to_child

    @pytest.mark.django_db
    def test_service_reads_from_database_correctly(self):
        """TreeService should read all members from database."""
        # Arrange
        from drzewo.models import Czlonek
        from drzewo.services import TreeService
        members = [
            Czlonek.objects.create(rok_chrztu=1960),
            Czlonek.objects.create(rok_chrztu=1962),
            Czlonek.objects.create(rok_chrztu=1985),
        ]
        service = TreeService()

        # Act
        tree_nodes = service.generate_full_tree()
        tree_member_ids = {node.member.pk for node in tree_nodes}

        # Assert
        for member in members:
            assert member.pk in tree_member_ids

    @pytest.mark.django_db
    def test_renderer_uses_member_data_correctly(self):
        """GraphRenderer should use member data in output."""
        # Arrange
        from drzewo.models import Czlonek, TreeNode
        from drzewo.rendering import GraphRenderer
        member = Czlonek.objects.create(pk=123, rok_chrztu=1960)
        nodes = [TreeNode(member=member, depth=0, layer=0)]
        edges = []
        renderer = GraphRenderer()

        # Act
        d3_data = renderer.build_d3_nodes(nodes, edges)

        # Assert
        assert len(d3_data["nodes"]) == 1
        assert d3_data["nodes"][0]["id"] == 123

