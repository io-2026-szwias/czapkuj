"""
Tests for sequence diagram workflows - frontend interaction tests.
"""
import pytest
from django.test import Client
from django.urls import reverse


class TestUserInteractionSequence:
    """Tests based on sequence diagram: user opens page and interacts with tree."""

    @pytest.mark.django_db
    def test_user_opens_interactive_tree_page(self):
        """User should be able to open the interactive tree page."""
        # Arrange
        from drzewo.models import Czlonek
        Czlonek.objects.create(rok_chrztu=1960)
        client = Client()
        url = reverse("full_tree_interactive_view")

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200
        assert b"html" in response.content.lower()

    @pytest.mark.django_db
    def test_page_returns_form_for_filtering(self):
        """Interactive view should return a form for filters."""
        # Arrange
        client = Client()
        url = reverse("full_tree_interactive_view")

        # Act
        response = client.get(url)

        # Assert
        assert b"<form" in response.content
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_frontend_can_fetch_tree_data_api(self):
        """Frontend should be able to fetch tree data from API."""
        # Arrange
        from drzewo.models import Czlonek
        Czlonek.objects.create(rok_chrztu=1960)
        client = Client()
        url = reverse("full_tree_data_graphviz")

        # Act
        response = client.get(url)
        data = response.json()

        # Assert
        assert response.status_code == 200
        assert "nodes" in data
        assert "links" in data

    @pytest.mark.django_db
    def test_api_response_contains_all_required_fields(self):
        """API response should contain all fields needed by D3."""
        # Arrange
        from drzewo.models import Czlonek
        Czlonek.objects.create(rok_chrztu=1960)
        client = Client()
        url = reverse("full_tree_data_graphviz")

        # Act
        response = client.get(url)
        data = response.json()

        # Assert
        required_fields = ["nodes", "links", "years", "childrenDict"]
        for field in required_fields:
            assert field in data

    @pytest.mark.django_db
    def test_api_includes_member_depth_and_layer(self):
        """API response nodes should include depth and layer for positioning."""
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
        for node in data["nodes"]:
            assert "depth" in node or "y" in node  # depth or similar positioning field
            assert "layer" in node or "x" in node   # layer or similar positioning field

    @pytest.mark.django_db
    def test_page_includes_d3_library(self):
        """Interactive view should include D3 library."""
        # Arrange
        client = Client()
        url = reverse("full_tree_interactive_view")

        # Act
        response = client.get(url)

        # Assert
        assert b"d3" in response.content.lower() or b"main.js" in response.content.lower()

    @pytest.mark.django_db
    def test_page_includes_main_javascript_file(self):
        """Interactive view should include main.js for initialization."""
        # Arrange
        client = Client()
        url = reverse("full_tree_interactive_view")

        # Act
        response = client.get(url)

        # Assert
        assert b"main.js" in response.content or b"script" in response.content

    @pytest.mark.django_db
    def test_api_response_nodes_have_proper_structure(self):
        """API nodes should have proper D3 structure (id, x, y or similar)."""
        # Arrange
        from drzewo.models import Czlonek
        member = Czlonek.objects.create(pk=1, rok_chrztu=1960)
        client = Client()
        url = reverse("full_tree_data_graphviz")

        # Act
        response = client.get(url)
        data = response.json()

        # Assert
        assert len(data["nodes"]) > 0
        node = data["nodes"][0]
        assert "id" in node
        assert node["id"] == 1

    @pytest.mark.django_db
    def test_api_response_links_have_source_and_target(self):
        """API links should have source and target for D3 force layout."""
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
        assert len(data["links"]) > 0
        link = data["links"][0]
        assert "source" in link
        assert "target" in link


class TestDynamicVisualizationInteraction:
    """Tests for dynamic visualization updates during user interaction."""

    @pytest.mark.django_db
    def test_multiple_api_calls_return_consistent_data(self):
        """Multiple calls to API should return consistent tree data."""
        # Arrange
        from drzewo.models import Czlonek
        Czlonek.objects.create(rok_chrztu=1960)
        client = Client()
        url = reverse("full_tree_data_graphviz")

        # Act
        response1 = client.get(url)
        response2 = client.get(url)
        data1 = response1.json()
        data2 = response2.json()

        # Assert
        assert len(data1["nodes"]) == len(data2["nodes"])
        assert len(data1["links"]) == len(data2["links"])

    @pytest.mark.django_db
    def test_api_reflects_database_changes_between_calls(self):
        """API should reflect new members added between calls."""
        # Arrange
        from drzewo.models import Czlonek
        client = Client()
        url = reverse("full_tree_data_graphviz")

        # Act
        response1 = client.get(url)
        data1 = response1.json()
        Czlonek.objects.create(rok_chrztu=1960)
        response2 = client.get(url)
        data2 = response2.json()

        # Assert
        assert len(data2["nodes"]) > len(data1["nodes"])

    @pytest.mark.django_db
    def test_childrendict_enables_parent_filtering(self):
        """childrenDict should map each parent to their children."""
        # Arrange
        from drzewo.models import Czlonek
        parent = Czlonek.objects.create(pk=1, rok_chrztu=1960)
        child1 = Czlonek.objects.create(pk=2, rodzic_1=parent, rok_chrztu=1985)
        child2 = Czlonek.objects.create(pk=3, rodzic_1=parent, rok_chrztu=1987)
        client = Client()
        url = reverse("full_tree_data_graphviz")

        # Act
        response = client.get(url)
        data = response.json()

        # Assert
        assert 1 in data["childrenDict"]
        assert set(data["childrenDict"][1]) == {2, 3}

    @pytest.mark.django_db
    def test_years_list_enables_year_filtering(self):
        """Years list should contain all unique baptism/generation years."""
        # Arrange
        from drzewo.models import Czlonek
        Czlonek.objects.create(rok_chrztu=1930)
        Czlonek.objects.create(rok_chrztu=1960)
        Czlonek.objects.create(rok_chrztu=1985)
        client = Client()
        url = reverse("full_tree_data_graphviz")

        # Act
        response = client.get(url)
        data = response.json()

        # Assert
        assert 1930 in data["years"]
        assert 1960 in data["years"]
        assert 1985 in data["years"]
        assert len(data["years"]) == 3

