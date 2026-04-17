import pytest
from django.test import Client
from dashboard.models import Zadanie, Status
from dashboard.services import TodoService, SearchService
from django.contrib.auth.models import User as DjangoUser


@pytest.mark.django_db
class TestTodoWorkflow:

    def test_create_list_complete_task_workflow(self, db, wielu_mistrz_user):
        """Test complete workflow: create task, list it, complete it"""
        service = TodoService()

        zadanie = Zadanie.objects.create(
            tytul="Integration Test Task",
            opis="Full workflow test",
            warunki="Must complete workflow",
            assigned_to=wielu_mistrz_user,
        )

        tasks = service.get_tasks()
        assert any(t.id == zadanie.id for t in tasks)

        retrieved = service.get_task(zadanie.id)
        assert retrieved.status == Status.TODO

        completed = service.complete_task(zadanie.id)
        assert completed.status == Status.DONE

    def test_task_with_dependencies_workflow(self, db, wielu_mistrz_user):
        """Test workflow: create tasks with dependencies"""
        service = TodoService()

        dep1 = Zadanie.objects.create(
            tytul="Dependency 1",
            opis="First dep",
            warunki="Must complete",
            assigned_to=wielu_mistrz_user,
        )
        dep2 = Zadanie.objects.create(
            tytul="Dependency 2",
            opis="Second dep",
            warunki="Must complete",
            assigned_to=wielu_mistrz_user,
        )
        main = Zadanie.objects.create(
            tytul="Main Task",
            opis="Has dependencies",
            warunki="Both deps required",
            assigned_to=wielu_mistrz_user,
        )

        service.add_dependency(main.id, dep1.id)
        service.add_dependency(main.id, dep2.id)

        retrieved_main = service.get_task(main.id)
        assert dep1 in retrieved_main.depends_on.all()
        assert dep2 in retrieved_main.depends_on.all()
        assert retrieved_main.depends_on.count() == 2

    def test_multiple_tasks_list_view_workflow(self, db, wielu_mistrz_user):
        """Test listing multiple tasks with mixed statuses"""
        service = TodoService()

        for i in range(5):
            Zadanie.objects.create(
                tytul=f"Task {i}",
                opis=f"Desc {i}",
                warunki="Cond",
                status=Status.TODO,
                assigned_to=wielu_mistrz_user,
            )

        for i in range(3):
            Zadanie.objects.create(
                tytul=f"Completed {i}",
                opis=f"Desc {i}",
                warunki="Cond",
                status=Status.DONE,
                assigned_to=wielu_mistrz_user,
            )

        all_tasks = service.get_tasks()
        assert len(all_tasks) == 8

    def test_complete_dependency_chain_workflow(self, db, wielu_mistrz_user):
        """Test completing tasks in dependency order"""
        service = TodoService()

        task_c = Zadanie.objects.create(
            tytul="Task C",
            opis="C",
            warunki="C",
            assigned_to=wielu_mistrz_user,
        )
        task_b = Zadanie.objects.create(
            tytul="Task B",
            opis="B",
            warunki="B",
            assigned_to=wielu_mistrz_user,
        )
        task_a = Zadanie.objects.create(
            tytul="Task A",
            opis="A",
            warunki="A",
            assigned_to=wielu_mistrz_user,
        )

        service.add_dependency(task_a.id, task_b.id)
        service.add_dependency(task_b.id, task_c.id)

        service.complete_task(task_c.id)
        service.complete_task(task_b.id)
        service.complete_task(task_a.id)

        final_a = Zadanie.objects.get(id=task_a.id)
        final_b = Zadanie.objects.get(id=task_b.id)
        final_c = Zadanie.objects.get(id=task_c.id)

        assert final_a.status == Status.DONE
        assert final_b.status == Status.DONE
        assert final_c.status == Status.DONE

    def test_add_multiple_dependencies_to_same_task(self, db, wielu_mistrz_user):
        """Test adding many dependencies to single task"""
        service = TodoService()

        main = Zadanie.objects.create(
            tytul="Main",
            opis="Main",
            warunki="Main",
            assigned_to=wielu_mistrz_user,
        )

        deps = []
        for i in range(5):
            dep = Zadanie.objects.create(
                tytul=f"Dep {i}",
                opis=f"Dep {i}",
                warunki="Dep",
                assigned_to=wielu_mistrz_user,
            )
            deps.append(dep)
            service.add_dependency(main.id, dep.id)

        final_main = service.get_task(main.id)
        assert final_main.depends_on.count() == 5


@pytest.mark.django_db
class TestSearchWorkflow:

    def test_search_find_user_by_email_workflow(self, db):
        """Test searching for user by email"""
        service = SearchService()

        user = DjangoUser.objects.create_user(
            username="testuser",
            email="john.developer@acmecorp.com",
        )

        results = service.search("john.developer@acmecorp.com")

        assert len(results) > 0
        assert any("john.developer" in r.get("email", "").lower() for r in results)

    def test_search_find_organization_workflow(self, db):
        """Test searching for organization"""
        service = SearchService()

        user = DjangoUser.objects.create_user(
            username="acmeadmin",
            email="admin@acmecorp.pl",
            first_name="ACME Admin",
        )

        results = service.search("ACME")

        assert len(results) > 0

    def test_search_multiple_results_workflow(self, db):
        """Test search returning multiple results"""
        service = SearchService()

        DjangoUser.objects.create_user(
            username="user1",
            email="search.user1@example.com",
        )
        DjangoUser.objects.create_user(
            username="user2",
            email="search.user2@example.com",
        )
        DjangoUser.objects.create_user(
            username="user3",
            email="search.user3@example.com",
        )

        results = service.search("search.user")

        assert len(results) >= 3

    def test_search_partial_email_workflow(self, db):
        """Test searching with partial email"""
        service = SearchService()

        DjangoUser.objects.create_user(
            username="developer",
            email="dev@mycompany.io",
        )

        results = service.search("dev@mycompany")

        assert len(results) > 0

    def test_search_case_insensitive_workflow(self, db):
        """Test that search is case insensitive"""
        service = SearchService()

        DjangoUser.objects.create_user(
            username="testuser",
            email="TestUser@EXAMPLE.COM",
        )

        results_lower = service.search("testuser@example.com")
        results_upper = service.search("TESTUSER@EXAMPLE.COM")
        results_mixed = service.search("TestUser@Example.Com")

        assert len(results_lower) > 0
        assert len(results_upper) > 0
        assert len(results_mixed) > 0


@pytest.mark.django_db
class TestTodoSearchIntegration:

    def test_search_then_assign_task_workflow(self, db, wielu_mistrz_user):
        """Test searching for user then assigning task"""
        search_service = SearchService()
        todo_service = TodoService()

        target_user = DjangoUser.objects.create_user(
            username="targetuser",
            email="target@organization.com",
        )

        search_results = search_service.search("target@organization")
        assert len(search_results) > 0

        task = Zadanie.objects.create(
            tytul="Assigned Task",
            opis="Found and assigned via search",
            warunki="Must complete",
            assigned_to=target_user,
        )

        retrieved = todo_service.get_task(task.id)
        assert retrieved.assigned_to == target_user

    def test_complete_workflow_search_to_task_completion(self, db, wielu_mistrz_user):
        """End-to-end: search user, create task, complete it"""
        search_service = SearchService()
        todo_service = TodoService()

        user = DjangoUser.objects.create_user(
            username="completionuser",
            email="completion@test.org",
        )

        search_results = search_service.search("completion@test.org")
        assert len(search_results) > 0

        task = Zadanie.objects.create(
            tytul="End-to-End Task",
            opis="From search to completion",
            warunki="Full workflow",
            assigned_to=user,
        )

        tasks = todo_service.get_tasks()
        assert any(t.id == task.id for t in tasks)

        completed = todo_service.complete_task(task.id)
        assert completed.status == Status.DONE

