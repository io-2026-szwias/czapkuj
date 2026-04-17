"""
README for Drzewo (Tree) Test Suite

This directory contains comprehensive pytest tests for the Tree/Drzewo family tree system.

## Test Files Overview

### Model Tests
- `test_czlonek_model.py` - Tests for Czlonek (Member) model
  - Fields: pk, rok_chrztu, staz, rodzic_1, rodzic_2
  - Methods: get_member_children(), get_member_step_children()

- `test_treenode_model.py` - Tests for TreeNode model
  - Fields: member, depth, year, layer
  - Methods: get_year(), get_layer()

- `test_bean_model.py` - Tests for Bean (alternative data source) model

### Service Tests
- `test_treeservice.py` - Tests for TreeService
  - Methods: build_layers_and_edges_from_db(), generate_full_tree()
  - Tests layer grouping, edge creation, depth/year/layer assignment

### Rendering Tests
- `test_graphrenderer.py` - Tests for GraphRenderer
  - Methods: render_layered_graph(), build_d3_nodes()
  - Tests D3 node/link structure, year collection, children mapping

### View/API Tests
- `test_drzewoview.py` - Tests for Django views and API endpoints
  - Methods: full_tree_interactive_view(), full_tree_data_graphviz()
  - Tests HTML/form response, JSON API response structure

### Integration Tests
- `test_integration_tree.py` - End-to-end workflow tests
  - Full tree building from database to API response
  - Multi-generation families, relationships, data consistency

- `test_sequence_workflows.py` - Workflow tests based on sequence diagrams
  - User interactions: opening page, fetching data
  - Frontend-backend interaction patterns
  - Dynamic visualization updates

### Edge Cases & Validation
- `test_edge_cases.py` - Edge case and error handling tests
  - Circular references, null values, large trees
  - Concurrent access, validation constraints

### Fixtures & Configuration
- `conftest.py` - Pytest fixtures and configuration
  - Shared fixtures for tree structures
  - Service and renderer instances

- `pytest.ini` - Pytest configuration
- `requirements.txt` - Test dependencies

## Running Tests

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run all tests
```bash
pytest
```

### Run specific test file
```bash
pytest test_czlonek_model.py
```

### Run specific test class
```bash
pytest test_czlonek_model.py::TestCzlonekModel
```

### Run specific test
```bash
pytest test_czlonek_model.py::TestCzlonekModel::test_czlonek_has_primary_key
```

### Run with verbose output
```bash
pytest -v
```

### Run with coverage
```bash
pytest --cov=drzewo --cov-report=html
```

### Run only integration tests
```bash
pytest test_integration_tree.py test_sequence_workflows.py
```

### Run only model tests
```bash
pytest test_*_model.py
```

## Test Philosophy

All tests follow **Test-Driven Development (TDD)** principles:

1. Tests are written BEFORE implementation
2. Tests define the expected behavior
3. Tests are currently **FAILING** (RED phase)
4. Implementation should make tests PASS (GREEN phase)
5. Then refactor while keeping tests green (REFACTOR phase)

## Test Organization

Tests are organized by:
- **Layer**: Models, Services, Views/APIs, Integration
- **Domain**: Czlonek, TreeNode, TreeService, GraphRenderer, DrzewoView
- **Concern**: Happy path, edge cases, error handling, performance

## Key Test Patterns

### Arrange-Act-Assert
Each test follows the AAA pattern:
```python
def test_example():
    # Arrange: Set up test data
    member = Czlonek.objects.create(rok_chrztu=1960)
    
    # Act: Perform the action
    children = member.get_member_children()
    
    # Assert: Verify the result
    assert len(children) == 0
```

### Database Fixtures
Tests requiring database access use `@pytest.mark.django_db`:
```python
@pytest.mark.django_db
def test_member_saved_to_database():
    member = Czlonek.objects.create(rok_chrztu=1960)
    assert Czlonek.objects.filter(rok_chrztu=1960).exists()
```

### Shared Fixtures
Common test data is provided via fixtures in `conftest.py`:
```python
def test_with_simple_tree(simple_tree_structure):
    assert simple_tree_structure["child1"].rodzic_1 == simple_tree_structure["parent1"]
```

## Mocking

Some tests use the `mocker` fixture (from pytest-mock) for:
- External API calls
- File I/O operations
- Third-party service interactions

Example:
```python
def test_with_mocked_graphviz(mocker):
    mock_render = mocker.patch("graphviz.Digraph.render")
    # Test code that calls graphviz
```

## Expected Behavior (from diagrams)

### Czlonek Model
- Has self-referential parent relationships (rodzic_1, rodzic_2)
- Can return direct children and step-children
- Each member has a baptism year (rok_chrztu)

### TreeNode Model
- Wraps Czlonek with layout information (depth, layer, year)
- Supports D3 visualization

### TreeService
- Reads members from database
- Builds hierarchical layers by generation depth
- Creates edges between parents and children
- Assigns positioning (depth, layer) to each node

### GraphRenderer
- Converts tree structure to Graphviz format
- Builds D3-compatible JSON structure
- Collects metadata (years, children mapping)

### DrzewoView
- Serves HTML page with form and D3 visualization
- Provides REST API endpoint returning JSON tree data
- API response includes: nodes, links, years, childrenDict

### Frontend Interaction
- User opens interactive page
- Frontend fetches data from API
- D3 renders interactive visualization
- User can filter, color, and interact with tree

## Notes for Implementation

1. Models must support self-referential parent relationships
2. Services should use database queries efficiently (consider prefetch_related)
3. API responses must include all required fields for D3 visualization
4. Edge cases like circular references should be handled gracefully
5. Large trees should perform efficiently (consider pagination or filtering)

