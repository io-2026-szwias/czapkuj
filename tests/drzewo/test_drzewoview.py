"""
Tests for DrzewoView API and view endpoints.
"""
import pytest
from django.test import Client
from django.urls import reverse


class TestDrzewoView:
    """Tests for DrzewoView Django views."""

    @pytest.mark.django_db
    def test_full_tree_interactive_view_returns_200(self):
        """GET /drzewo/full-tree-interactive/ should return 200 OK."""
        # Arrange
        client = Client()
        url = reverse("full_tree_interactive_view")  # Adjust URL name as needed

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_full_tree_interactive_view_returns_html(self):
        """full_tree_interactive_view() should return HTML response."""
        # Arrange
        client = Client()
        url = reverse("full_tree_interactive_view")

        # Act
        response = client.get(url)

        # Assert
        assert "text/html" in response["Content-Type"]

    @pytest.mark.django_db
    def test_full_tree_interactive_view_includes_form(self):
        """full_tree_interactive_view() should include form in response."""
        # Arrange
        client = Client()
        url = reverse("full_tree_interactive_view")

        # Act
        response = client.get(url)

        # Assert
        assert b"<form" in response.content

    @pytest.mark.django_db
    def test_full_tree_interactive_view_includes_js_assets(self):
        """full_tree_interactive_view() should include JavaScript assets."""
        # Arrange
        client = Client()
        url = reverse("full_tree_interactive_view")

        # Act
        response = client.get(url)

        # Assert
        assert b"<script" in response.content or b".js" in response.content

    @pytest.mark.django_db
    def test_full_tree_data_graphviz_returns_json(self):
        """GET /full-tree-data/ should return JSON response."""
        # Arrange
        client = Client()
        url = reverse("full_tree_data_graphviz")  # Adjust URL name as needed

        # Act
        response = client.get(url)

        # Assert
        assert response["Content-Type"] == "application/json" or "json" in response["Content-Type"]
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_full_tree_data_graphviz_returns_nodes(self):
        """full_tree_data_graphviz() should return 'nodes' in JSON."""
        # Arrange
        from drzewo.models import Czlonek
        Czlonek.objects.create(rok_chrztu=1960)
        client = Client()
        url = reverse("full_tree_data_graphviz")

        # Act
        response = client.get(url)
        data = response.json()

        # Assert
        assert "nodes" in data
        assert isinstance(data["nodes"], list)

    @pytest.mark.django_db
    def test_full_tree_data_graphviz_returns_links(self):
        """full_tree_data_graphviz() should return 'links' in JSON."""
        # Arrange
        client = Client()
        url = reverse("full_tree_data_graphviz")

        # Act
        response = client.get(url)
        data = response.json()

        # Assert
        assert "links" in data
        assert isinstance(data["links"], list)

    @pytest.mark.django_db
    def test_full_tree_data_graphviz_returns_years(self):
        """full_tree_data_graphviz() should return 'years' in JSON."""
        # Arrange
        client = Client()
        url = reverse("full_tree_data_graphviz")

        # Act
        response = client.get(url)
        data = response.json()

        # Assert
        assert "years" in data
        assert isinstance(data["years"], list)

    @pytest.mark.django_db
    def test_full_tree_data_graphviz_returns_children_dict(self):
        """full_tree_data_graphviz() should return 'childrenDict' in JSON."""
        # Arrange
        client = Client()
        url = reverse("full_tree_data_graphviz")

        # Act
        response = client.get(url)
        data = response.json()

        # Assert
        assert "childrenDict" in data
        assert isinstance(data["childrenDict"], dict)

    @pytest.mark.django_db
    def test_full_tree_data_graphviz_includes_all_members(self):
        """full_tree_data_graphviz() should include all members in tree data."""
        # Arrange
        from drzewo.models import Czlonek
        member1 = Czlonek.objects.create(rok_chrztu=1960)
        member2 = Czlonek.objects.create(rok_chrztu=1985)
        client = Client()
        url = reverse("full_tree_data_graphviz")

        # Act
        response = client.get(url)
        data = response.json()

        # Assert
        member_ids = [node["id"] for node in data["nodes"]]
        assert member1.pk in member_ids
        assert member2.pk in member_ids

    @pytest.mark.django_db
    def test_full_tree_data_graphviz_includes_relationships(self):
        """full_tree_data_graphviz() should include parent-child relationships in links."""
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
        link_pairs = [(link["source"], link["target"]) for link in data["links"]]
        assert (parent.pk, child.pk) in link_pairs

    @pytest.mark.django_db
    def test_full_tree_interactive_view_loads_successfully(self):
        """User should be able to load the interactive tree page."""
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
    def test_full_tree_data_graphviz_empty_database(self):
        """full_tree_data_graphviz() should handle empty database gracefully."""
        # Arrange
        client = Client()
        url = reverse("full_tree_data_graphviz")

        # Act
        response = client.get(url)
        data = response.json()

        # Assert
        assert response.status_code == 200
        assert len(data["nodes"]) == 0
        assert len(data["links"]) == 0

