"""
Tests for Zdarzenie (Occurrence) model.
"""
import pytest
from datetime import date, time


class TestZdarzenie:
    """Tests for Occurrence model."""

    @pytest.mark.django_db
    def test_zdarzenie_has_nazwa_field(self):
        """Zdarzenie should have nazwa (name) field."""
        # Arrange
        from kalendarz.models import Zdarzenie

        # Act
        occurrence = Zdarzenie.objects.create(
            nazwa="Morning Service"
        )

        # Assert
        assert occurrence.nazwa == "Morning Service"

    @pytest.mark.django_db
    def test_zdarzenie_has_data_field(self):
        """Zdarzenie should have data (date) field."""
        # Arrange
        from kalendarz.models import Zdarzenie
        event_date = date(2026, 5, 15)

        # Act
        occurrence = Zdarzenie.objects.create(
            nazwa="Service",
            data=event_date
        )

        # Assert
        assert occurrence.data == event_date

    @pytest.mark.django_db
    def test_zdarzenie_has_godzina_field(self):
        """Zdarzenie should have godzina (time) field."""
        # Arrange
        from kalendarz.models import Zdarzenie
        event_time = time(10, 30)

        # Act
        occurrence = Zdarzenie.objects.create(
            nazwa="Service",
            data=date(2026, 5, 15),
            godzina=event_time
        )

        # Assert
        assert occurrence.godzina == event_time

    @pytest.mark.django_db
    def test_zdarzenie_has_opis_field(self):
        """Zdarzenie should have opis (description) field."""
        # Arrange
        from kalendarz.models import Zdarzenie

        # Act
        occurrence = Zdarzenie.objects.create(
            nazwa="Service",
            data=date(2026, 5, 15),
            opis="Morning service with choir"
        )

        # Assert
        assert occurrence.opis == "Morning service with choir"

    @pytest.mark.django_db
    def test_zdarzenie_related_to_miejsca(self):
        """Zdarzenie can be associated with a place (miejsce)."""
        # Arrange
        from kalendarz.models import Zdarzenie, Miejsce
        place = Miejsce.objects.create(nazwa="Church")

        # Act
        occurrence = Zdarzenie.objects.create(
            nazwa="Service",
            data=date(2026, 5, 15),
            miejsce=place
        )

        # Assert
        assert occurrence.miejsce == place

    @pytest.mark.django_db
    def test_zdarzenie_can_have_related_people(self):
        """Zdarzenie can be associated with related people."""
        # Arrange
        from kalendarz.models import Zdarzenie, Osoba
        osoba = Osoba.objects.create(imie="Jan", nazwisko="Nowak")

        # Act
        occurrence = Zdarzenie.objects.create(
            nazwa="Service",
            data=date(2026, 5, 15)
        )
        occurrence.powiazane_osoby.add(osoba)

        # Assert
        assert osoba in occurrence.powiazane_osoby.all()

    @pytest.mark.django_db
    def test_multiple_occurrences_can_belong_to_calendar_event(self):
        """Multiple occurrences can belong to one calendar event."""
        # Arrange
        from kalendarz.models import WydarzenieKalendarzowe, Zdarzenie
        event = WydarzenieKalendarzowe.objects.create(
            nazwa="Festival",
            data_rozpoczecia=date(2026, 5, 15)
        )

        # Act
        occ1 = Zdarzenie.objects.create(
            nazwa="Opening",
            data=date(2026, 5, 15),
            godzina=time(9, 0),
            wydarzenie_kalendarzowe=event
        )
        occ2 = Zdarzenie.objects.create(
            nazwa="Closing",
            data=date(2026, 5, 15),
            godzina=time(18, 0),
            wydarzenie_kalendarzowe=event
        )

        # Assert
        occurrences = Zdarzenie.objects.filter(wydarzenie_kalendarzowe=event)
        assert occurrences.count() == 2

    @pytest.mark.django_db
    def test_godzina_field_is_optional(self):
        """godzina field should be optional."""
        # Arrange
        from kalendarz.models import Zdarzenie

        # Act
        occurrence = Zdarzenie.objects.create(
            nazwa="All-day event",
            data=date(2026, 5, 15),
            godzina=None
        )

        # Assert
        assert occurrence.godzina is None

    @pytest.mark.django_db
    def test_opis_field_is_optional(self):
        """opis field should be optional."""
        # Arrange
        from kalendarz.models import Zdarzenie

        # Act
        occurrence = Zdarzenie.objects.create(
            nazwa="Service",
            data=date(2026, 5, 15),
            opis=None
        )

        # Assert
        assert occurrence.opis is None

    @pytest.mark.django_db
    def test_multiple_people_related_to_occurrence(self):
        """Multiple people can be associated with one occurrence."""
        # Arrange
        from kalendarz.models import Zdarzenie, Osoba
        osoba1 = Osoba.objects.create(imie="Jan", nazwisko="Nowak")
        osoba2 = Osoba.objects.create(imie="Anna", nazwisko="Kowalski")

        # Act
        occurrence = Zdarzenie.objects.create(
            nazwa="Service",
            data=date(2026, 5, 15)
        )
        occurrence.powiazane_osoby.add(osoba1, osoba2)

        # Assert
        assert occurrence.powiazane_osoby.count() == 2

