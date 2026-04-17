"""
Pytest configuration file with shared fixtures for Tree/Drzewo tests.
"""
import pytest
from django.contrib.auth.models import User


@pytest.fixture
def django_db_setup(django_db_setup, django_db_blocker):
    """Setup Django test database."""
    with django_db_blocker.unblock():
        pass


@pytest.fixture
def test_user(db):
    """Create a test user."""
    return User.objects.create_user(
        username="testuser",
        email="test@example.com",
        password="testpass123"
    )


@pytest.fixture
def simple_tree_structure(db):
    """
    Create a simple tree structure:

    grandparent (1930)
        ├─ parent1 (1960)
        │   └─ child1 (1985)
        └─ parent2 (1962)
            └─ child2 (1987)
    """
    from drzewo.models import Czlonek
    grandparent = Czlonek.objects.create(rok_chrztu=1930)
    parent1 = Czlonek.objects.create(rodzic_1=grandparent, rok_chrztu=1960)
    parent2 = Czlonek.objects.create(rodzic_1=grandparent, rok_chrztu=1962)
    child1 = Czlonek.objects.create(rodzic_1=parent1, rok_chrztu=1985)
    child2 = Czlonek.objects.create(rodzic_1=parent2, rok_chrztu=1987)
    return {
        "grandparent": grandparent,
        "parent1": parent1,
        "parent2": parent2,
        "child1": child1,
        "child2": child2,
    }


@pytest.fixture
def deep_tree_structure(db):
    """
    Create a deep tree structure (4 generations):

    root (1900)
        └─ gen1 (1930)
            └─ gen2 (1960)
                └─ gen3 (1985)
    """
    from drzewo.models import Czlonek
    root = Czlonek.objects.create(rok_chrztu=1900)
    gen1 = Czlonek.objects.create(rodzic_1=root, rok_chrztu=1930)
    gen2 = Czlonek.objects.create(rodzic_1=gen1, rok_chrztu=1960)
    gen3 = Czlonek.objects.create(rodzic_1=gen2, rok_chrztu=1985)
    return {
        "root": root,
        "gen1": gen1,
        "gen2": gen2,
        "gen3": gen3,
    }


@pytest.fixture
def wide_tree_structure(db):
    """
    Create a wide tree structure with many siblings:

    parent (1960)
        ├─ child1 (1985)
        ├─ child2 (1987)
        ├─ child3 (1990)
        ├─ child4 (1992)
        └─ child5 (1995)
    """
    from drzewo.models import Czlonek
    parent = Czlonek.objects.create(rok_chrztu=1960)
    children = [
        Czlonek.objects.create(rodzic_1=parent, rok_chrztu=1985),
        Czlonek.objects.create(rodzic_1=parent, rok_chrztu=1987),
        Czlonek.objects.create(rodzic_1=parent, rok_chrztu=1990),
        Czlonek.objects.create(rodzic_1=parent, rok_chrztu=1992),
        Czlonek.objects.create(rodzic_1=parent, rok_chrztu=1995),
    ]
    return {"parent": parent, "children": children}


@pytest.fixture
def tree_service(db):
    """Instantiate TreeService."""
    from drzewo.services import TreeService
    return TreeService()


@pytest.fixture
def graph_renderer(db):
    """Instantiate GraphRenderer."""
    from drzewo.rendering import GraphRenderer
    return GraphRenderer()


@pytest.fixture
def django_client():
    """Provide Django test client."""
    from django.test import Client
    return Client()

