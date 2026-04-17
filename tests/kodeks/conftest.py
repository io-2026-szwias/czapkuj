"""
Pytest configuration and fixtures for Kodeks tests.
"""
import pytest


@pytest.fixture
def sample_podmiot(db):
    """Create a sample entity."""
    from kodeks.models import Podmiot
    return Podmiot.objects.create(nazwa="Sample Entity", aktualne=True)


@pytest.fixture
def sample_role(db):
    """Create a sample role."""
    from kodeks.models import Rola
    return Rola.objects.create(nazwa="Sample Role", aktualne=True)


@pytest.fixture
def sample_struktura(db):
    """Create a sample structure."""
    from kodeks.models import Struktura
    return Struktura.objects.create(nazwa="Sample Structure", aktualne=True)


@pytest.fixture
def sample_section(db):
    """Create a sample section."""
    from kodeks.models import KodeksSection
    return KodeksSection.objects.create(nazwa="Sample Section", kolejnosc=1)


@pytest.fixture
def sample_relacja(db):
    """Create a sample legal relationship."""
    from kodeks.models import RelacjaPrawna
    return RelacjaPrawna.objects.create(
        tresc="Sample legal content",
        prawo_czy_obowiazek="right"
    )


@pytest.fixture
def sample_dokument(db):
    """Create a sample document."""
    from kodeks.models import Dokument
    return Dokument.objects.create(nazwa="Sample Document")


@pytest.fixture
def sample_rule(db, sample_section, sample_relacja, sample_podmiot):
    """Create a sample rule with relationships."""
    from kodeks.models import PrawoObowiazek
    return PrawoObowiazek.objects.create(
        aktualne=True,
        dotyczy=sample_podmiot,
        opisuje=sample_relacja,
        należy_do=sample_section
    )


@pytest.fixture
def multiple_sections(db):
    """Create multiple sections in order."""
    from kodeks.models import KodeksSection
    sections = []
    for i in range(1, 6):
        section = KodeksSection.objects.create(
            nazwa=f"Chapter {i}",
            kolejnosc=i
        )
        sections.append(section)
    return sections


@pytest.fixture
def multiple_rules(db, sample_section, sample_relacja):
    """Create multiple active rules."""
    from kodeks.models import PrawoObowiazek
    rules = []
    for i in range(5):
        rule = PrawoObowiazek.objects.create(
            aktualne=True,
            opisuje=sample_relacja,
            należy_do=sample_section
        )
        rules.append(rule)
    return rules


@pytest.fixture
def mixed_entities(db):
    """Create a mix of different entity types."""
    from kodeks.models import Rola, Struktura, Podmiot
    entities = {
        'roles': [],
        'structures': [],
        'general': []
    }
    
    for i in range(3):
        role = Rola.objects.create(nazwa=f"Role {i}", aktualne=True)
        entities['roles'].append(role)
    
    for i in range(2):
        structure = Struktura.objects.create(nazwa=f"Structure {i}", aktualne=True)
        entities['structures'].append(structure)
    
    for i in range(2):
        entity = Podmiot.objects.create(nazwa=f"General Entity {i}", aktualne=True)
        entities['general'].append(entity)
    
    return entities


@pytest.fixture
def complex_kodeks(db):
    """Create a complex kodeks structure with sections, rules, and entities."""
    from kodeks.models import (
        KodeksSection, PrawoObowiazek, RelacjaPrawna, 
        Podmiot, Dokument, Rola
    )
    
    # Create sections
    sections = [
        KodeksSection.objects.create(nazwa="Chapter 1", kolejnosc=1),
        KodeksSection.objects.create(nazwa="Chapter 2", kolejnosc=2),
    ]
    
    # Create entities
    role = Rola.objects.create(nazwa="President", aktualne=True)
    entity = Podmiot.objects.create(nazwa="Board", aktualne=True)
    
    # Create relationships
    relacja = RelacjaPrawna.objects.create(
        tresc="Complex legal content",
        prawo_czy_obowiazek="right"
    )
    
    # Create document
    dokument = Dokument.objects.create(nazwa="Main Law")
    
    # Create rules
    rules = [
        PrawoObowiazek.objects.create(
            aktualne=True,
            dotyczy=role,
            należy_do=sections[0],
            opisuje=relacja,
            źródło=dokument
        ),
        PrawoObowiazek.objects.create(
            aktualne=True,
            dotyczy=entity,
            należy_do=sections[1],
            opisuje=relacja,
            źródło=dokument
        ),
    ]
    
    return {
        'sections': sections,
        'entities': [role, entity],
        'rules': rules,
        'dokument': dokument
    }

