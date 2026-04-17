"""
Tests for RelacjaPrawna (Legal Relationship) model.
"""
import pytest


class TestRelacjaPrawna:
    """Tests for Legal Relationship model."""

    @pytest.mark.django_db
    def test_relacja_prawna_has_tresc_field(self):
        """RelacjaPrawna should have tresc (content) field."""
        # Arrange
        from kodeks.models import RelacjaPrawna
        
        # Act
        relationship = RelacjaPrawna.objects.create(
            tresc="Legal content"
        )

        # Assert
        assert relationship.tresc == "Legal content"

    @pytest.mark.django_db
    def test_relacja_prawna_has_prawo_czy_obowiazek_field(self):
        """RelacjaPrawna should have prawo_czy_obowiazek (right or obligation) field."""
        # Arrange
        from kodeks.models import RelacjaPrawna
        
        # Act
        relationship = RelacjaPrawna.objects.create(
            tresc="Content",
            prawo_czy_obowiazek="right"
        )

        # Assert
        assert relationship.prawo_czy_obowiazek == "right"

    @pytest.mark.django_db
    def test_relacja_prawna_prawo_czy_obowiazek_can_be_obligation(self):
        """prawo_czy_obowiazek can be set to obligation."""
        # Arrange
        from kodeks.models import RelacjaPrawna
        
        # Act
        relationship = RelacjaPrawna.objects.create(
            tresc="Content",
            prawo_czy_obowiazek="obligation"
        )

        # Assert
        assert relationship.prawo_czy_obowiazek == "obligation"

    @pytest.mark.django_db
    def test_create_multiple_relationships(self):
        """Should be able to create multiple relationships."""
        # Arrange
        from kodeks.models import RelacjaPrawna
        
        # Act
        rel1 = RelacjaPrawna.objects.create(
            tresc="Right content",
            prawo_czy_obowiazek="right"
        )
        rel2 = RelacjaPrawna.objects.create(
            tresc="Obligation content",
            prawo_czy_obowiazek="obligation"
        )

        # Assert
        assert RelacjaPrawna.objects.count() == 2

    @pytest.mark.django_db
    def test_query_rights(self):
        """Should be able to query relationships of type 'right'."""
        # Arrange
        from kodeks.models import RelacjaPrawna
        RelacjaPrawna.objects.create(tresc="Right 1", prawo_czy_obowiazek="right")
        RelacjaPrawna.objects.create(tresc="Obligation", prawo_czy_obowiazek="obligation")
        RelacjaPrawna.objects.create(tresc="Right 2", prawo_czy_obowiazek="right")

        # Act
        rights = RelacjaPrawna.objects.filter(prawo_czy_obowiazek="right")

        # Assert
        assert rights.count() == 2

    @pytest.mark.django_db
    def test_query_obligations(self):
        """Should be able to query relationships of type 'obligation'."""
        # Arrange
        from kodeks.models import RelacjaPrawna
        RelacjaPrawna.objects.create(tresc="Right", prawo_czy_obowiazek="right")
        RelacjaPrawna.objects.create(tresc="Obligation 1", prawo_czy_obowiazek="obligation")
        RelacjaPrawna.objects.create(tresc="Obligation 2", prawo_czy_obowiazek="obligation")

        # Act
        obligations = RelacjaPrawna.objects.filter(prawo_czy_obowiazek="obligation")

        # Assert
        assert obligations.count() == 2

    @pytest.mark.django_db
    def test_relacja_prawna_with_long_content(self):
        """RelacjaPrawna can contain long text content."""
        # Arrange
        from kodeks.models import RelacjaPrawna
        long_content = "This is a very long legal text that explains " * 10
        
        # Act
        relationship = RelacjaPrawna.objects.create(
            tresc=long_content,
            prawo_czy_obowiazek="right"
        )

        # Assert
        assert len(relationship.tresc) > 100
        assert relationship.tresc == long_content

