"""
Tests for KodeksSection (Code Section) model.
"""
import pytest


class TestKodeksSection:
    """Tests for Code Section model."""

    @pytest.mark.django_db
    def test_kodeks_section_has_nazwa_field(self):
        """KodeksSection should have nazwa (name) field."""
        # Arrange
        from kodeks.models import KodeksSection
        
        # Act
        section = KodeksSection.objects.create(
            nazwa="Chapter 1",
            kolejnosc=1
        )

        # Assert
        assert section.nazwa == "Chapter 1"

    @pytest.mark.django_db
    def test_kodeks_section_has_kolejnosc_field(self):
        """KodeksSection should have kolejnosc (order) field."""
        # Arrange
        from kodeks.models import KodeksSection
        
        # Act
        section = KodeksSection.objects.create(
            nazwa="Section",
            kolejnosc=5
        )

        # Assert
        assert section.kolejnosc == 5

    @pytest.mark.django_db
    def test_create_multiple_sections(self):
        """Should be able to create multiple sections."""
        # Arrange
        from kodeks.models import KodeksSection
        
        # Act
        section1 = KodeksSection.objects.create(nazwa="Chapter 1", kolejnosc=1)
        section2 = KodeksSection.objects.create(nazwa="Chapter 2", kolejnosc=2)

        # Assert
        assert KodeksSection.objects.count() == 2

    @pytest.mark.django_db
    def test_sections_can_be_ordered_by_kolejnosc(self):
        """Sections should be retrievable ordered by kolejnosc."""
        # Arrange
        from kodeks.models import KodeksSection
        KodeksSection.objects.create(nazwa="Chapter 3", kolejnosc=3)
        KodeksSection.objects.create(nazwa="Chapter 1", kolejnosc=1)
        KodeksSection.objects.create(nazwa="Chapter 2", kolejnosc=2)

        # Act
        ordered_sections = list(KodeksSection.objects.order_by('kolejnosc'))

        # Assert
        assert ordered_sections[0].kolejnosc == 1
        assert ordered_sections[1].kolejnosc == 2
        assert ordered_sections[2].kolejnosc == 3
        assert ordered_sections[0].nazwa == "Chapter 1"

    @pytest.mark.django_db
    def test_sections_ordered_by_kolejnosc_retrieves_in_order(self):
        """Ordered query should return sections in sequence."""
        # Arrange
        from kodeks.models import KodeksSection
        for i in range(1, 6):
            KodeksSection.objects.create(nazwa=f"Section {i}", kolejnosc=i)

        # Act
        sections = KodeksSection.objects.all().order_by('kolejnosc')

        # Assert
        assert sections.count() == 5
        for i, section in enumerate(sections, 1):
            assert section.kolejnosc == i

    @pytest.mark.django_db
    def test_section_with_zero_order(self):
        """Section can have kolejnosc of 0."""
        # Arrange
        from kodeks.models import KodeksSection
        
        # Act
        section = KodeksSection.objects.create(
            nazwa="Preamble",
            kolejnosc=0
        )

        # Assert
        assert section.kolejnosc == 0

    @pytest.mark.django_db
    def test_section_with_large_order_number(self):
        """Section can have large kolejnosc values."""
        # Arrange
        from kodeks.models import KodeksSection
        
        # Act
        section = KodeksSection.objects.create(
            nazwa="Appendix",
            kolejnosc=999
        )

        # Assert
        assert section.kolejnosc == 999

    @pytest.mark.django_db
    def test_query_section_by_order_range(self):
        """Should be able to query sections by order range."""
        # Arrange
        from kodeks.models import KodeksSection
        for i in range(1, 11):
            KodeksSection.objects.create(nazwa=f"Section {i}", kolejnosc=i)

        # Act
        middle_sections = KodeksSection.objects.filter(kolejnosc__gte=4, kolejnosc__lte=7)

        # Assert
        assert middle_sections.count() == 4

