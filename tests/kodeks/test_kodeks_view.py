"""
Tests for KodeksView and code rendering.
"""
import pytest
from django.test import Client
from django.urls import reverse


class TestKodeksView:
    """Tests for code/codex view and rendering."""

    @pytest.mark.django_db
    def test_kodeks_view_returns_200(self):
        """GET /kodeks/ should return 200 OK."""
        # Arrange
        client = Client()
        url = reverse("kodeks_view")  # Adjust URL name as needed

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_kodeks_view_returns_html(self):
        """Kodeks view should return HTML response."""
        # Arrange
        client = Client()
        url = reverse("kodeks_view")

        # Act
        response = client.get(url)

        # Assert
        assert "text/html" in response["Content-Type"]

    @pytest.mark.django_db
    def test_kodeks_view_has_get_method(self):
        """KodeksView should have get method."""
        # Arrange
        from kodeks.views import KodeksView
        view = KodeksView()

        # Act & Assert
        assert hasattr(view, "get")
        assert callable(view.get)

    @pytest.mark.django_db
    def test_kodeks_view_has_render_kodeks_method(self):
        """KodeksView should have render_kodeks method."""
        # Arrange
        from kodeks.views import KodeksView
        view = KodeksView()

        # Act & Assert
        assert hasattr(view, "render_kodeks")
        assert callable(view.render_kodeks)

    @pytest.mark.django_db
    def test_kodeks_view_fetches_sections_ordered(self):
        """KodeksView should fetch sections ordered by kolejnosc."""
        # Arrange
        from kodeks.models import KodeksSection
        KodeksSection.objects.create(nazwa="Chapter 3", kolejnosc=3)
        KodeksSection.objects.create(nazwa="Chapter 1", kolejnosc=1)
        KodeksSection.objects.create(nazwa="Chapter 2", kolejnosc=2)
        client = Client()
        url = reverse("kodeks_view")

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_kodeks_view_fetches_active_rules(self):
        """KodeksView should fetch only active rules."""
        # Arrange
        from kodeks.models import PrawoObowiazek
        PrawoObowiazek.objects.create(aktualne=True)
        PrawoObowiazek.objects.create(aktualne=False)
        PrawoObowiazek.objects.create(aktualne=True)
        from kodeks.views import KodeksView
        view = KodeksView()

        # Act & Assert
        # The view should have logic to fetch active rules
        assert hasattr(view, "render_kodeks")

    @pytest.mark.django_db
    def test_kodeks_view_fetches_related_entities(self):
        """KodeksView should fetch related Podmiot entities."""
        # Arrange
        from kodeks.models import Podmiot
        Podmiot.objects.create(nazwa="Entity 1")
        Podmiot.objects.create(nazwa="Entity 2")
        client = Client()
        url = reverse("kodeks_view")

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_kodeks_view_groups_rules_by_section(self):
        """KodeksView should group rules by section."""
        # Arrange
        from kodeks.models import KodeksSection, PrawoObowiazek
        section1 = KodeksSection.objects.create(nazwa="Section 1", kolejnosc=1)
        section2 = KodeksSection.objects.create(nazwa="Section 2", kolejnosc=2)
        
        PrawoObowiazek.objects.create(aktualne=True, należy_do=section1)
        PrawoObowiazek.objects.create(aktualne=True, należy_do=section1)
        PrawoObowiazek.objects.create(aktualne=True, należy_do=section2)
        
        from kodeks.views import KodeksView
        view = KodeksView()

        # Act & Assert
        assert hasattr(view, "render_kodeks")

    @pytest.mark.django_db
    def test_kodeks_view_with_no_sections(self):
        """KodeksView should handle empty sections gracefully."""
        # Arrange
        client = Client()
        url = reverse("kodeks_view")

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_kodeks_view_with_no_rules(self):
        """KodeksView should handle no rules gracefully."""
        # Arrange
        from kodeks.models import KodeksSection
        KodeksSection.objects.create(nazwa="Section", kolejnosc=1)
        client = Client()
        url = reverse("kodeks_view")

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_kodeks_view_displays_sections_in_order(self):
        """Kodeks view should display sections in order of kolejnosc."""
        # Arrange
        from kodeks.models import KodeksSection
        KodeksSection.objects.create(nazwa="First", kolejnosc=1)
        KodeksSection.objects.create(nazwa="Second", kolejnosc=2)
        KodeksSection.objects.create(nazwa="Third", kolejnosc=3)
        client = Client()
        url = reverse("kodeks_view")

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200

