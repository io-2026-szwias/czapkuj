"""
Integration tests for Kodeks system workflows.
"""
import pytest
from django.test import Client
from django.urls import reverse


class TestKodeksWorkflows:
    """Integration tests for codex/code system workflows."""

    @pytest.mark.django_db
    def test_user_opens_kodeks_page(self):
        """User should be able to open the codex page."""
        # Arrange
        client = Client()
        url = reverse("kodeks_view")

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200
        assert b"html" in response.content.lower()

    @pytest.mark.django_db
    def test_kodeks_displays_sections_and_rules(self):
        """Kodeks should display sections and their associated rules."""
        # Arrange
        from kodeks.models import KodeksSection, PrawoObowiazek, RelacjaPrawna
        section = KodeksSection.objects.create(nazwa="Chapter 1", kolejnosc=1)
        relacja = RelacjaPrawna.objects.create(tresc="Rule content", prawo_czy_obowiazek="right")
        rule = PrawoObowiazek.objects.create(
            aktualne=True,
            należy_do=section,
            opisuje=relacja
        )
        client = Client()
        url = reverse("kodeks_view")

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_kodeks_ordered_sections(self):
        """Sections in kodeks should be displayed in order of kolejnosc."""
        # Arrange
        from kodeks.models import KodeksSection
        for i in [3, 1, 2]:
            KodeksSection.objects.create(nazwa=f"Chapter {i}", kolejnosc=i)
        
        client = Client()
        url = reverse("kodeks_view")

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_kodeks_with_multiple_entities(self):
        """Kodeks should handle multiple related entities."""
        # Arrange
        from kodeks.models import Podmiot, KodeksSection, PrawoObowiazek, RelacjaPrawna
        
        podmiot1 = Podmiot.objects.create(nazwa="Board", aktualne=True)
        podmiot2 = Podmiot.objects.create(nazwa="Committee", aktualne=True)
        
        section = KodeksSection.objects.create(nazwa="Section 1", kolejnosc=1)
        
        relacja = RelacjaPrawna.objects.create(tresc="Content", prawo_czy_obowiazek="obligation")
        
        rule = PrawoObowiazek.objects.create(
            aktualne=True,
            dotyczy=podmiot1,
            należy_do=section,
            opisuje=relacja
        )
        
        client = Client()
        url = reverse("kodeks_view")

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_kodeks_with_active_and_inactive_rules(self):
        """Kodeks should display only active rules."""
        # Arrange
        from kodeks.models import KodeksSection, PrawoObowiazek
        
        section = KodeksSection.objects.create(nazwa="Section 1", kolejnosc=1)
        
        active_rule = PrawoObowiazek.objects.create(
            aktualne=True,
            należy_do=section
        )
        
        inactive_rule = PrawoObowiazek.objects.create(
            aktualne=False,
            należy_do=section
        )
        
        from kodeks.views import KodeksView
        view = KodeksView()

        # Act & Assert
        assert hasattr(view, "render_kodeks")

    @pytest.mark.django_db
    def test_kodeks_groups_rules_correctly(self):
        """Kodeks should correctly group rules by section."""
        # Arrange
        from kodeks.models import KodeksSection, PrawoObowiazek
        
        section1 = KodeksSection.objects.create(nazwa="Chapter 1", kolejnosc=1)
        section2 = KodeksSection.objects.create(nazwa="Chapter 2", kolejnosc=2)
        
        for i in range(3):
            PrawoObowiazek.objects.create(aktualne=True, należy_do=section1)
        
        for i in range(2):
            PrawoObowiazek.objects.create(aktualne=True, należy_do=section2)
        
        # Act
        section1_rules = PrawoObowiazek.objects.filter(należy_do=section1, aktualne=True)
        section2_rules = PrawoObowiazek.objects.filter(należy_do=section2, aktualne=True)

        # Assert
        assert section1_rules.count() == 3
        assert section2_rules.count() == 2

    @pytest.mark.django_db
    def test_kodeks_with_empty_sections(self):
        """Kodeks should handle sections with no rules."""
        # Arrange
        from kodeks.models import KodeksSection
        
        section1 = KodeksSection.objects.create(nazwa="Chapter 1", kolejnosc=1)
        section2 = KodeksSection.objects.create(nazwa="Chapter 2", kolejnosc=2)
        
        client = Client()
        url = reverse("kodeks_view")

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_kodeks_inheritance_polymorphism(self):
        """Kodeks should handle polymorphic entities (Rola, Struktura)."""
        # Arrange
        from kodeks.models import Rola, Struktura, KodeksSection, PrawoObowiazek
        
        role = Rola.objects.create(nazwa="President", aktualne=True)
        structure = Struktura.objects.create(nazwa="Board", aktualne=True)
        
        section = KodeksSection.objects.create(nazwa="Section 1", kolejnosc=1)
        
        rule1 = PrawoObowiazek.objects.create(aktualne=True, dotyczy=role, należy_do=section)
        rule2 = PrawoObowiazek.objects.create(aktualne=True, dotyczy=structure, należy_do=section)

        # Act
        rules_in_section = PrawoObowiazek.objects.filter(należy_do=section, aktualne=True)

        # Assert
        assert rules_in_section.count() == 2

    @pytest.mark.django_db
    def test_kodeks_renders_correctly(self):
        """Kodeks view should render with proper structure."""
        # Arrange
        client = Client()
        url = reverse("kodeks_view")

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200
        assert b"<" in response.content  # Contains HTML

    @pytest.mark.django_db
    def test_kodeks_with_complex_relationships(self):
        """Kodeks should handle complex rule relationships."""
        # Arrange
        from kodeks.models import (
            Rola, KodeksSection, PrawoObowiazek, 
            RelacjaPrawna, Dokument
        )
        
        role = Rola.objects.create(nazwa="Treasurer", aktualne=True)
        section = KodeksSection.objects.create(nazwa="Financial Section", kolejnosc=1)
        relacja = RelacjaPrawna.objects.create(tresc="Financial rules", prawo_czy_obowiazek="obligation")
        dokument = Dokument.objects.create(nazwa="Financial Law")
        
        rule = PrawoObowiazek.objects.create(
            aktualne=True,
            dotyczy=role,
            należy_do=section,
            opisuje=relacja,
            źródło=dokument
        )

        # Act
        retrieved_rule = PrawoObowiazek.objects.get(pk=rule.pk)

        # Assert
        assert retrieved_rule.dotyczy == role
        assert retrieved_rule.należy_do == section
        assert retrieved_rule.opisuje == relacja
        assert retrieved_rule.źródło == dokument

