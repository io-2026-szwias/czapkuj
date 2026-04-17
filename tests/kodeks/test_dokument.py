"""
Tests for Dokument (Document) model.
"""
import pytest


class TestDokument:
    """Tests for Document model."""

    @pytest.mark.django_db
    def test_dokument_has_nazwa_field(self):
        """Dokument should have nazwa (name) field."""
        # Arrange
        from kodeks.models import Dokument
        
        # Act
        document = Dokument.objects.create(nazwa="Constitution")

        # Assert
        assert document.nazwa == "Constitution"

    @pytest.mark.django_db
    def test_create_multiple_documents(self):
        """Should be able to create multiple documents."""
        # Arrange
        from kodeks.models import Dokument
        
        # Act
        doc1 = Dokument.objects.create(nazwa="Constitution")
        doc2 = Dokument.objects.create(nazwa="Statute")

        # Assert
        assert Dokument.objects.count() == 2

    @pytest.mark.django_db
    def test_document_referenced_by_rules(self):
        """Document can be referenced by rules as source."""
        # Arrange
        from kodeks.models import Dokument, PrawoObowiazek
        document = Dokument.objects.create(nazwa="Law Document")
        
        # Act
        rule = PrawoObowiazek.objects.create(
            aktualne=True,
            źródło=document
        )

        # Assert
        assert rule.źródło == document

    @pytest.mark.django_db
    def test_multiple_rules_can_reference_same_document(self):
        """Multiple rules can reference the same document."""
        # Arrange
        from kodeks.models import Dokument, PrawoObowiazek
        document = Dokument.objects.create(nazwa="Master Document")
        
        # Act
        rule1 = PrawoObowiazek.objects.create(aktualne=True, źródło=document)
        rule2 = PrawoObowiazek.objects.create(aktualne=True, źródło=document)
        rule3 = PrawoObowiazek.objects.create(aktualne=True, źródło=document)

        # Assert
        rules_with_doc = PrawoObowiazek.objects.filter(źródło=document)
        assert rules_with_doc.count() == 3

