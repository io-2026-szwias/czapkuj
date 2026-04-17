"""
Tests for related models: Miejsce, Osoba, Dokument, TypWydarzenia, TypWyjazdu.
"""
import pytest
from datetime import date


class TestMiejsce:
    """Tests for Miejsce (Place) model."""

    @pytest.mark.django_db
    def test_miejsce_has_nazwa_field(self):
        """Miejsce should have nazwa (name) field."""
        # Arrange
        from kalendarz.models import Miejsce

        # Act
        place = Miejsce.objects.create(nazwa="Church")

        # Assert
        assert place.nazwa == "Church"

    @pytest.mark.django_db
    def test_create_multiple_places(self):
        """Should be able to create multiple places."""
        # Arrange
        from kalendarz.models import Miejsce

        # Act
        place1 = Miejsce.objects.create(nazwa="Church")
        place2 = Miejsce.objects.create(nazwa="Hall")

        # Assert
        assert Miejsce.objects.count() == 2


class TestOsoba:
    """Tests for Osoba (Person) model."""

    @pytest.mark.django_db
    def test_osoba_has_imie_field(self):
        """Osoba should have imie (first name) field."""
        # Arrange
        from kalendarz.models import Osoba

        # Act
        person = Osoba.objects.create(imie="Jan", nazwisko="Nowak")

        # Assert
        assert person.imie == "Jan"

    @pytest.mark.django_db
    def test_osoba_has_nazwisko_field(self):
        """Osoba should have nazwisko (last name) field."""
        # Arrange
        from kalendarz.models import Osoba

        # Act
        person = Osoba.objects.create(imie="Jan", nazwisko="Nowak")

        # Assert
        assert person.nazwisko == "Nowak"

    @pytest.mark.django_db
    def test_create_multiple_people(self):
        """Should be able to create multiple people."""
        # Arrange
        from kalendarz.models import Osoba

        # Act
        person1 = Osoba.objects.create(imie="Jan", nazwisko="Nowak")
        person2 = Osoba.objects.create(imie="Anna", nazwisko="Kowalski")

        # Assert
        assert Osoba.objects.count() == 2


class TestDokument:
    """Tests for Dokument (Document) model."""

    @pytest.mark.django_db
    def test_dokument_has_nazwa_field(self):
        """Dokument should have nazwa (name) field."""
        # Arrange
        from kalendarz.models import Dokument

        # Act
        document = Dokument.objects.create(nazwa="Baptism Certificate")

        # Assert
        assert document.nazwa == "Baptism Certificate"

    @pytest.mark.django_db
    def test_create_multiple_documents(self):
        """Should be able to create multiple documents."""
        # Arrange
        from kalendarz.models import Dokument

        # Act
        doc1 = Dokument.objects.create(nazwa="Certificate")
        doc2 = Dokument.objects.create(nazwa="Report")

        # Assert
        assert Dokument.objects.count() == 2


class TestTypWydarzenia:
    """Tests for TypWydarzenia (Event Type) model."""

    @pytest.mark.django_db
    def test_typ_wydarzenia_has_typ_field(self):
        """TypWydarzenia should have typ (type) field."""
        # Arrange
        from kalendarz.models import TypWydarzenia

        # Act
        event_type = TypWydarzenia.objects.create(typ="Service")

        # Assert
        assert event_type.typ == "Service"

    @pytest.mark.django_db
    def test_create_multiple_event_types(self):
        """Should be able to create multiple event types."""
        # Arrange
        from kalendarz.models import TypWydarzenia

        # Act
        type1 = TypWydarzenia.objects.create(typ="Service")
        type2 = TypWydarzenia.objects.create(typ="Meeting")

        # Assert
        assert TypWydarzenia.objects.count() == 2

    @pytest.mark.django_db
    def test_event_can_have_type(self):
        """Event can be associated with event type."""
        # Arrange
        from kalendarz.models import Wydarzenie, TypWydarzenia
        event_type = TypWydarzenia.objects.create(typ="Service")

        # Act
        event = Wydarzenie.objects.create(
            nazwa="Event",
            data_rozpoczecia=date.today(),
            typ_wydarzenia=event_type
        )

        # Assert
        assert event.typ_wydarzenia == event_type


class TestTypWyjazdu:
    """Tests for TypWyjazdu (Trip Type) model."""

    @pytest.mark.django_db
    def test_typ_wyjazdu_has_typ_field(self):
        """TypWyjazdu should have typ (type) field."""
        # Arrange
        from kalendarz.models import TypWyjazdu

        # Act
        trip_type = TypWyjazdu.objects.create(typ="Pilgrimage")

        # Assert
        assert trip_type.typ == "Pilgrimage"

    @pytest.mark.django_db
    def test_create_multiple_trip_types(self):
        """Should be able to create multiple trip types."""
        # Arrange
        from kalendarz.models import TypWyjazdu

        # Act
        type1 = TypWyjazdu.objects.create(typ="Pilgrimage")
        type2 = TypWyjazdu.objects.create(typ="Mission")

        # Assert
        assert TypWyjazdu.objects.count() == 2

    @pytest.mark.django_db
    def test_event_can_have_trip_type(self):
        """Trip event can be associated with trip type."""
        # Arrange
        from kalendarz.models import Wydarzenie, TypWyjazdu
        trip_type = TypWyjazdu.objects.create(typ="Pilgrimage")

        # Act
        event = Wydarzenie.objects.create(
            nazwa="Trip",
            data_rozpoczecia=date.today(),
            czy_to_wyjazd=True,
            typ_wyjazdu=trip_type
        )

        # Assert
        assert event.typ_wyjazdu == trip_type


class TestRelationships:
    """Tests for model relationships."""

    @pytest.mark.django_db
    def test_event_has_multiple_places(self):
        """Event can be associated with multiple places."""
        # Arrange
        from kalendarz.models import Wydarzenie, Miejsce
        place1 = Miejsce.objects.create(nazwa="Church")
        place2 = Miejsce.objects.create(nazwa="Hall")

        # Act
        event = Wydarzenie.objects.create(
            nazwa="Event",
            data_rozpoczecia=date.today()
        )
        event.miejsca.add(place1, place2)

        # Assert
        assert event.miejsca.count() == 2

    @pytest.mark.django_db
    def test_event_has_multiple_attendees(self):
        """Event can have multiple attendees."""
        # Arrange
        from kalendarz.models import Wydarzenie, Osoba
        osoba1 = Osoba.objects.create(imie="Jan", nazwisko="Nowak")
        osoba2 = Osoba.objects.create(imie="Anna", nazwisko="Kowalski")

        # Act
        event = Wydarzenie.objects.create(
            nazwa="Event",
            data_rozpoczecia=date.today()
        )
        event.uczestnicy.add(osoba1, osoba2)

        # Assert
        assert event.uczestnicy.count() == 2

