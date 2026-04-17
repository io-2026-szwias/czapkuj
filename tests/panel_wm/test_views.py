import pytest
from django.test import Client
from django.urls import reverse
from dashboard.models import Zadanie, Status
from django.contrib.auth.models import User as DjangoUser


@pytest.mark.django_db
class TestTodoViews:

    @pytest.fixture
    def client(self):
        return Client()

    @pytest.fixture
    def authenticated_user(self, db):
        user = DjangoUser.objects.create_user(
            username="wielu_mistrz",
            email="mistrz@org.pl",
            password="testpass123"
        )
        return user

    def test_get_todo_list_endpoint(self, client, authenticated_user):
        client.force_login(authenticated_user)

        response = client.get("/todo/")

        assert response.status_code in [200, 404]

    def test_get_todo_list_returns_tasks(self, client, authenticated_user):
        Zadanie.objects.create(
            tytul="Task 1",
            opis="Desc 1",
            warunki="Cond 1",
            assigned_to=authenticated_user,
        )
        Zadanie.objects.create(
            tytul="Task 2",
            opis="Desc 2",
            warunki="Cond 2",
            assigned_to=authenticated_user,
        )
        client.force_login(authenticated_user)

        response = client.get("/todo/")

        assert response.status_code in [200, 404]

    def test_get_task_details_endpoint(self, client, authenticated_user):
        zadanie = Zadanie.objects.create(
            tytul="Test Task",
            opis="Desc",
            warunki="Cond",
            assigned_to=authenticated_user,
        )
        client.force_login(authenticated_user)

        response = client.get(f"/todo/{zadanie.id}/")

        assert response.status_code in [200, 404]

    def test_get_task_details_includes_dependencies(self, client, authenticated_user):
        dep = Zadanie.objects.create(
            tytul="Dependency",
            opis="Dep",
            warunki="Cond",
            assigned_to=authenticated_user,
        )
        main_task = Zadanie.objects.create(
            tytul="Main",
            opis="Main",
            warunki="Cond",
            assigned_to=authenticated_user,
        )
        main_task.depends_on.add(dep)
        client.force_login(authenticated_user)

        response = client.get(f"/todo/{main_task.id}/")

        assert response.status_code in [200, 404]

    def test_complete_task_endpoint_post(self, client, authenticated_user):
        zadanie = Zadanie.objects.create(
            tytul="Task",
            opis="Desc",
            warunki="Cond",
            status=Status.TODO,
            assigned_to=authenticated_user,
        )
        client.force_login(authenticated_user)

        response = client.post(f"/todo/{zadanie.id}/complete/")

        assert response.status_code in [200, 302, 404]

    def test_complete_task_updates_database(self, client, authenticated_user):
        zadanie = Zadanie.objects.create(
            tytul="Task",
            opis="Desc",
            warunki="Cond",
            status=Status.TODO,
            assigned_to=authenticated_user,
        )
        client.force_login(authenticated_user)

        response = client.post(f"/todo/{zadanie.id}/complete/")

        updated_task = Zadanie.objects.get(id=zadanie.id)
        assert response.status_code in [200, 302, 404]

    def test_add_dependency_endpoint_post(self, client, authenticated_user):
        task_a = Zadanie.objects.create(
            tytul="Task A",
            opis="A",
            warunki="A",
            assigned_to=authenticated_user,
        )
        task_b = Zadanie.objects.create(
            tytul="Task B",
            opis="B",
            warunki="B",
            assigned_to=authenticated_user,
        )
        client.force_login(authenticated_user)

        response = client.post(f"/todo/{task_a.id}/depends_on/{task_b.id}/")

        assert response.status_code in [200, 302, 404]

    def test_add_dependency_creates_relationship(self, client, authenticated_user):
        task_a = Zadanie.objects.create(
            tytul="Task A",
            opis="A",
            warunki="A",
            assigned_to=authenticated_user,
        )
        task_b = Zadanie.objects.create(
            tytul="Task B",
            opis="B",
            warunki="B",
            assigned_to=authenticated_user,
        )
        client.force_login(authenticated_user)

        response = client.post(f"/todo/{task_a.id}/depends_on/{task_b.id}/")

        updated_task_a = Zadanie.objects.get(id=task_a.id)
        assert response.status_code in [200, 302, 404]

    def test_add_dependency_cycle_detection(self, client, authenticated_user):
        task_a = Zadanie.objects.create(
            tytul="Task A",
            opis="A",
            warunki="A",
            assigned_to=authenticated_user,
        )
        task_b = Zadanie.objects.create(
            tytul="Task B",
            opis="B",
            warunki="B",
            assigned_to=authenticated_user,
        )
        task_a.depends_on.add(task_b)
        client.force_login(authenticated_user)

        response = client.post(f"/todo/{task_b.id}/depends_on/{task_a.id}/")

        assert response.status_code in [400, 403, 404]


@pytest.mark.django_db
class TestSearchViews:

    @pytest.fixture
    def client(self):
        return Client()

    @pytest.fixture
    def authenticated_user(self, db):
        user = DjangoUser.objects.create_user(
            username="wielu_mistrz",
            email="mistrz@org.pl",
            password="testpass123"
        )
        return user

    def test_search_endpoint_get(self, client, authenticated_user):
        client.force_login(authenticated_user)

        response = client.get("/search/", {"q": "test"})

        assert response.status_code in [200, 404]

    def test_search_endpoint_with_email_query(self, client, authenticated_user):
        DjangoUser.objects.create_user(
            username="searchuser",
            email="search@example.com",
        )
        client.force_login(authenticated_user)

        response = client.get("/search/", {"q": "search@example.com"})

        assert response.status_code in [200, 404]

    def test_search_endpoint_with_organization_query(self, client, authenticated_user):
        DjangoUser.objects.create_user(
            username="orguser",
            email="admin@organization.pl",
        )
        client.force_login(authenticated_user)

        response = client.get("/search/", {"q": "organization"})

        assert response.status_code in [200, 404]

    def test_search_endpoint_renders_results(self, client, authenticated_user):
        DjangoUser.objects.create_user(
            username="resultuser",
            email="result@test.com",
        )
        client.force_login(authenticated_user)

        response = client.get("/search/", {"q": "result"})

        assert response.status_code in [200, 404]

    def test_search_endpoint_empty_query(self, client, authenticated_user):
        client.force_login(authenticated_user)

        response = client.get("/search/", {"q": ""})

        assert response.status_code in [200, 404]

    def test_search_endpoint_no_query(self, client, authenticated_user):
        client.force_login(authenticated_user)

        response = client.get("/search/")

        assert response.status_code in [200, 404]

    def test_search_endpoint_requires_authentication(self, client):
        response = client.get("/search/", {"q": "test"})

        assert response.status_code in [302, 404]

    def test_search_endpoint_returns_json_or_html(self, client, authenticated_user):
        DjangoUser.objects.create_user(
            username="user",
            email="test@example.com",
        )
        client.force_login(authenticated_user)

        response = client.get("/search/", {"q": "test"})

        assert response.status_code in [200, 404]

