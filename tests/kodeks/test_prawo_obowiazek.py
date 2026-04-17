"""
Tests for PrawoObowiazek (Right/Obligation) model.
"""
import pytest


class TestPrawoObowiazek:
    """Tests for Right/Obligation model."""

    @pytest.mark.django_db
    def test_prawo_obowiazek_has_aktualne_field(self):
        """PrawoObowiazek should have aktualne (is_active) field."""
        # Arrange
        from kodeks.models import PrawoObowiazek
        
        # Act
        rule = PrawoObowiazek.objects.create(aktualne=True)

        # Assert
        assert rule.aktualne is True

    @pytest.mark.django_db
    def test_prawo_obowiazek_can_be_inactive(self):
        """PrawoObowiazek can be marked as inactive."""
        # Arrange
        from kodeks.models import PrawoObowiazek
        
        # Act
        rule = PrawoObowiazek.objects.create(aktualne=False)

        # Assert
        assert rule.aktualne is False

    @pytest.mark.django_db
    def test_prawo_obowiazek_related_to_podmiot(self):
        """PrawoObowiazek should be related to Podmiot."""
        # Arrange
        from kodeks.models import PrawoObowiazek, Podmiot
        podmiot = Podmiot.objects.create(nazwa="Entity")
        
        # Act
        rule = PrawoObowiazek.objects.create(
            aktualne=True,
            dotyczy=podmiot
        )

        # Assert
        assert rule.dotyczy == podmiot

    @pytest.mark.django_db
    def test_prawo_obowiazek_related_to_relacja_prawna(self):
        """PrawoObowiazek should be related to RelacjaPrawna."""
        # Arrange
        from kodeks.models import PrawoObowiazek, RelacjaPrawna
        relacja = RelacjaPrawna.objects.create(
            tresc="Legal content",
            prawo_czy_obowiazek="right"
        )
        
        # Act
        rule = PrawoObowiazek.objects.create(
            aktualne=True,
            opisuje=relacja
        )

        # Assert
        assert rule.opisuje == relacja

    @pytest.mark.django_db
    def test_prawo_obowiazek_related_to_dokument(self):
        """PrawoObowiazek should be related to Dokument."""
        # Arrange
        from kodeks.models import PrawoObowiazek, Dokument
        dokument = Dokument.objects.create(nazwa="Law Document")
        
        # Act
        rule = PrawoObowiazek.objects.create(
            aktualne=True,
            źródło=dokument
        )

        # Assert
        assert rule.źródło == dokument

    @pytest.mark.django_db
    def test_prawo_obowiazek_related_to_kodeks_section(self):
        """PrawoObowiazek should be related to KodeksSection."""
        # Arrange
        from kodeks.models import PrawoObowiazek, KodeksSection
        section = KodeksSection.objects.create(nazwa="Section 1", kolejnosc=1)
        
        # Act
        rule = PrawoObowiazek.objects.create(
            aktualne=True,
            należy_do=section
        )

        # Assert
        assert rule.należy_do == section

    @pytest.mark.django_db
    def test_query_active_rules(self):
        """Should be able to query active rules."""
        # Arrange
        from kodeks.models import PrawoObowiazek
        PrawoObowiazek.objects.create(aktualne=True)
        PrawoObowiazek.objects.create(aktualne=False)
        PrawoObowiazek.objects.create(aktualne=True)

        # Act
        active_rules = PrawoObowiazek.objects.filter(aktualne=True)

        # Assert
        assert active_rules.count() == 2

    @pytest.mark.django_db
    def test_query_inactive_rules(self):
        """Should be able to query inactive rules."""
        # Arrange
        from kodeks.models import PrawoObowiazek
        PrawoObowiazek.objects.create(aktualne=True)
        PrawoObowiazek.objects.create(aktualne=False)

        # Act
        inactive_rules = PrawoObowiazek.objects.filter(aktualne=False)

        # Assert
        assert inactive_rules.count() == 1

    @pytest.mark.django_db
    def test_rules_in_section(self):
        """Should be able to query rules in a specific section."""
        # Arrange
        from kodeks.models import PrawoObowiazek, KodeksSection
        section1 = KodeksSection.objects.create(nazwa="Section 1", kolejnosc=1)
        section2 = KodeksSection.objects.create(nazwa="Section 2", kolejnosc=2)
        
        PrawoObowiazek.objects.create(aktualne=True, należy_do=section1)
        PrawoObowiazek.objects.create(aktualne=True, należy_do=section1)
        PrawoObowiazek.objects.create(aktualne=True, należy_do=section2)

        # Act
        section1_rules = PrawoObowiazek.objects.filter(należy_do=section1)

        # Assert
        assert section1_rules.count() == 2

    @pytest.mark.django_db
    def test_complete_rule_with_all_relationships(self):
        """Should be able to create a rule with all relationships."""
        # Arrange
        from kodeks.models import PrawoObowiazek, Podmiot, RelacjaPrawna, Dokument, KodeksSection
        podmiot = Podmiot.objects.create(nazwa="Entity")
        relacja = RelacjaPrawna.objects.create(tresc="Content", prawo_czy_obowiazek="right")
        dokument = Dokument.objects.create(nazwa="Document")
        section = KodeksSection.objects.create(nazwa="Section", kolejnosc=1)
        
        # Act
        rule = PrawoObowiazek.objects.create(
            aktualne=True,
            dotyczy=podmiot,
            opisuje=relacja,
            źródło=dokument,
            należy_do=section
        )

        # Assert
        assert rule.dotyczy == podmiot
        assert rule.opisuje == relacja
        assert rule.źródło == dokument
        assert rule.należy_do == section
        assert rule.aktualne is True

