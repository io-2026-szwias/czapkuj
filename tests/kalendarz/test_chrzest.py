"""
Tests for Chrzest (Baptism) model.
"""
import pytest
from datetime import date


class TestChrzest:
    """Tests for Baptism event model (inherits from WydarzenieKalendarzowe)."""

    @pytest.mark.django_db
    def test_chrzest_has_miejsce_field(self):
        """Chrzest should have miejsce (place) field."""
        # Arrange
        from kalendarz.models import Chrzest, Miejsce
        place = Miejsce.objects.create(nazwa="Church")

        # Act
        baptism = Chrzest.objects.create(
            nazwa="Baptism",
            data_rozpoczecia=date(2026, 5, 15),
            miejsce=place
        )

        # Assert
        assert baptism.miejsce == place

    @pytest.mark.django_db
    def test_chrzest_inherits_from_calendar_event(self):
        """Chrzest should inherit fields from WydarzenieKalendarzowe."""
        # Arrange
        from kalendarz.models import Chrzest

        # Act
        baptism = Chrzest.objects.create(
            nazwa="Baptism Event",
            data_rozpoczecia=date(2026, 5, 15),
            link="https://example.com/baptism",
            opis="Spring baptism"
        )

        # Assert
        assert baptism.nazwa == "Baptism Event"
        assert baptism.link == "https://example.com/baptism"
        assert baptism.opis == "Spring baptism"

    @pytest.mark.django_db
    def test_chrzest_can_have_chrzczeni_osoba(self):
        """Chrzest should be associated with people being baptized."""
        # Arrange
        from kalendarz.models import Chrzest, Osoba
        osoba = Osoba.objects.create(imie="Jan", nazwisko="Nowak")

        # Act
        baptism = Chrzest.objects.create(
            nazwa="Baptism",
            data_rozpoczecia=date(2026, 5, 15)
        )
        baptism.chrzczeni.add(osoba)

        # Assert
        assert osoba in baptism.chrzczeni.all()

    @pytest.mark.django_db
    def test_chrzest_can_have_hymn_singer(self):
        """Chrzest can be associated with a person singing hymn."""
        # Arrange
        from kalendarz.models import Chrzest, Osoba
        hymn_singer = Osoba.objects.create(imie="Maria", nazwisko="Kowalski")

        # Act
        baptism = Chrzest.objects.create(
            nazwa="Baptism",
            data_rozpoczecia=date(2026, 5, 15),
            hymn=hymn_singer
        )

        # Assert
        assert baptism.hymn == hymn_singer

    @pytest.mark.django_db
    def test_chrzest_can_have_dokument(self):
        """Chrzest can be associated with a document."""
        # Arrange
        from kalendarz.models import Chrzest, Dokument
        dokument = Dokument.objects.create(nazwa="Baptism Certificate")

        # Act
        baptism = Chrzest.objects.create(
            nazwa="Baptism",
            data_rozpoczecia=date(2026, 5, 15),
            dokument=dokument
        )

        # Assert
        assert baptism.dokument == dokument

    @pytest.mark.django_db
    def test_multiple_people_can_be_baptized_in_one_event(self):
        """Multiple people can be baptized in a single baptism event."""
        # Arrange
        from kalendarz.models import Chrzest, Osoba
        osoba1 = Osoba.objects.create(imie="Jan", nazwisko="Nowak")
        osoba2 = Osoba.objects.create(imie="Anna", nazwisko="Kowalski")

        # Act
        baptism = Chrzest.objects.create(
            nazwa="Baptism",
            data_rozpoczecia=date(2026, 5, 15)
        )
        baptism.chrzczeni.add(osoba1, osoba2)

        # Assert
        assert baptism.chrzczeni.count() == 2
        assert osoba1 in baptism.chrzczeni.all()
        assert osoba2 in baptism.chrzczeni.all()

    @pytest.mark.django_db
    def test_chrzest_powiazane_osoby_field(self):
        """Chrzest inherits powiazane_osoby through Zdarzenie relationship."""
        # Arrange
        from kalendarz.models import Chrzest, Osoba
        osoba = Osoba.objects.create(imie="Jan", nazwisko="Nowak")

        # Act
        baptism = Chrzest.objects.create(
            nazwa="Baptism",
            data_rozpoczecia=date(2026, 5, 15)
        )
        baptism.chrzczeni.add(osoba)

        # Assert
        assert osoba in baptism.chrzczeni.all()

    @pytest.mark.django_db
    def test_dokument_field_is_optional(self):
        """dokument field should be optional."""
        # Arrange
        from kalendarz.models import Chrzest

        # Act
        baptism = Chrzest.objects.create(
            nazwa="Baptism",
            data_rozpoczecia=date(2026, 5, 15),
            dokument=None
        )

        # Assert
        assert baptism.dokument is None

    @pytest.mark.django_db
    def test_hymn_field_is_optional(self):
        """hymn field should be optional."""
        # Arrange
        from kalendarz.models import Chrzest

        # Act
        baptism = Chrzest.objects.create(
            nazwa="Baptism",
            data_rozpoczecia=date(2026, 5, 15),
            hymn=None
        )

        # Assert
        assert baptism.hymn is None

