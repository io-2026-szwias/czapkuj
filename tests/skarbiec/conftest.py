import pytest
from django.contrib.auth.models import User as DjangoUser


@pytest.fixture
def skarbnik_user(db):
    return DjangoUser.objects.create_user(
        username="skarbnik",
        email="skarbnik@org.pl",
        password="securepass",
    )


@pytest.fixture
def member_user(db):
    return DjangoUser.objects.create_user(
        username="member",
        email="member@org.pl",
        password="securepass",
    )


@pytest.fixture
def member_user_2(db):
    return DjangoUser.objects.create_user(
        username="member2",
        email="member2@org.pl",
        password="securepass",
    )


@pytest.fixture
def konto(db, member_user):
    from skarbiec.models import Konto
    return Konto.objects.create(
        user=member_user,
        numer_konta="12345678901234567890",
        numer_telefonu="+48123456789",
        nazwa_wlasciciela="Jan Kowalski",
    )


@pytest.fixture
def cel_skladkowy(db):
    from skarbiec.models import CelSkladkowy, CelStatus
    return CelSkladkowy.objects.create(
        tytul="Test Collection Goal",
        opis="Test contribution goal",
        termin="2025-12-31",
        kod="TEST001",
        status=CelStatus.OPEN,
    )


@pytest.fixture
def cel_skladkowy_closed(db):
    from skarbiec.models import CelSkladkowy, CelStatus
    return CelSkladkowy.objects.create(
        tytul="Closed Goal",
        opis="Already closed goal",
        termin="2024-01-01",
        kod="CLOSED001",
        status=CelStatus.CLOSED,
    )


@pytest.fixture
def cel_platnik(db, cel_skladkowy, member_user):
    from skarbiec.models import CelSkladkowyPlatnik, PlatnikStatus
    return CelSkladkowyPlatnik.objects.create(
        cel_skladkowy=cel_skladkowy,
        platnik=member_user,
        kwota_docelowa=100.00,
        kwota_zaplacona=0.00,
        status=PlatnikStatus.NIEZAPLACONE,
    )


@pytest.fixture
def transakcja(db, konto):
    from skarbiec.models import Transakcja
    return Transakcja.objects.create(
        data="2025-01-15",
        kwota=100.00,
        tytul="Transfer TEST001",
        nr_konta=konto.numer_konta,
        nadawca="Jan Kowalski",
    )


@pytest.fixture
def import_sesja(db):
    from skarbiec.models import ImportSesja, ImportStatus
    return ImportSesja.objects.create(
        data_importu="2025-01-15",
        nazwa_pliku="transactions.csv",
        status=ImportStatus.SUCCESS,
    )


@pytest.fixture
def multiple_cel_skladkowy(db):
    from skarbiec.models import CelSkladkowy, CelStatus
    cels = []
    for i in range(5):
        cel = CelSkladkowy.objects.create(
            tytul=f"Goal {i}",
            opis=f"Description {i}",
            termin="2025-12-31",
            kod=f"GOAL{i:03d}",
            status=CelStatus.OPEN,
        )
        cels.append(cel)
    return cels


@pytest.fixture
def multiple_platnicy(db, cel_skladkowy):
    from skarbiec.models import CelSkladkowyPlatnik, PlatnikStatus
    platnicy = []
    for i in range(5):
        user = DjangoUser.objects.create_user(
            username=f"user{i}",
            email=f"user{i}@org.pl",
        )
        platnik = CelSkladkowyPlatnik.objects.create(
            cel_skladkowy=cel_skladkowy,
            platnik=user,
            kwota_docelowa=50.00 + i * 10,
            kwota_zaplacona=0.00,
            status=PlatnikStatus.NIEZAPLACONE,
        )
        platnicy.append(platnik)
    return platnicy

