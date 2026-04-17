import pytest
from dashboard.services import TodoService
from dashboard.models import Zadanie, Status


@pytest.mark.django_db
class TestTodoService:

    def test_get_tasks_returns_all_tasks(self, db, wielu_mistrz_user):
        Zadanie.objects.create(
            tytul="Task 1",
            opis="Desc 1",
            warunki="Cond 1",
            assigned_to=wielu_mistrz_user,
        )
        Zadanie.objects.create(
            tytul="Task 2",
            opis="Desc 2",
            warunki="Cond 2",
            assigned_to=wielu_mistrz_user,
        )

        service = TodoService()
        tasks = service.get_tasks()

        assert len(tasks) == 2
        assert all(isinstance(t, Zadanie) for t in tasks)

    def test_get_tasks_includes_dependencies(self, db, wielu_mistrz_user):
        dep_task = Zadanie.objects.create(
            tytul="Dependency",
            opis="Dep",
            warunki="Cond",
            assigned_to=wielu_mistrz_user,
        )
        main_task = Zadanie.objects.create(
            tytul="Main Task",
            opis="Main",
            warunki="Cond",
            assigned_to=wielu_mistrz_user,
        )
        main_task.depends_on.add(dep_task)

        service = TodoService()
        tasks = service.get_tasks()

        retrieved_main = [t for t in tasks if t.id == main_task.id][0]
        assert dep_task in retrieved_main.depends_on.all()

    def test_get_task_by_id(self, db, wielu_mistrz_user):
        zadanie = Zadanie.objects.create(
            tytul="Test Task",
            opis="Description",
            warunki="Conditions",
            assigned_to=wielu_mistrz_user,
        )

        service = TodoService()
        retrieved = service.get_task(zadanie.id)

        assert retrieved.id == zadanie.id
        assert retrieved.tytul == "Test Task"

    def test_get_task_includes_dependencies(self, db, wielu_mistrz_user):
        dep1 = Zadanie.objects.create(
            tytul="Dependency 1",
            opis="Dep 1",
            warunki="Cond",
            assigned_to=wielu_mistrz_user,
        )
        dep2 = Zadanie.objects.create(
            tytul="Dependency 2",
            opis="Dep 2",
            warunki="Cond",
            assigned_to=wielu_mistrz_user,
        )
        main_task = Zadanie.objects.create(
            tytul="Main Task",
            opis="Main",
            warunki="Cond",
            assigned_to=wielu_mistrz_user,
        )
        main_task.depends_on.add(dep1, dep2)

        service = TodoService()
        retrieved = service.get_task(main_task.id)

        assert dep1 in retrieved.depends_on.all()
        assert dep2 in retrieved.depends_on.all()

    def test_complete_task_updates_status(self, db, zadanie_todo):
        service = TodoService()
        service.complete_task(zadanie_todo.id)

        updated_task = Zadanie.objects.get(id=zadanie_todo.id)
        assert updated_task.status == Status.DONE

    def test_complete_task_sets_completed_at(self, db, zadanie_todo):
        service = TodoService()
        service.complete_task(zadanie_todo.id)

        updated_task = Zadanie.objects.get(id=zadanie_todo.id)
        assert updated_task.completed_at is not None

    def test_complete_task_returns_updated_task(self, db, zadanie_todo):
        service = TodoService()
        result = service.complete_task(zadanie_todo.id)

        assert result.id == zadanie_todo.id
        assert result.status == Status.DONE

    def test_add_dependency_creates_relationship(self, db, wielu_mistrz_user):
        task_a = Zadanie.objects.create(
            tytul="Task A",
            opis="A",
            warunki="A",
            assigned_to=wielu_mistrz_user,
        )
        task_b = Zadanie.objects.create(
            tytul="Task B",
            opis="B",
            warunki="B",
            assigned_to=wielu_mistrz_user,
        )

        service = TodoService()
        service.add_dependency(task_a.id, task_b.id)

        updated_task_a = Zadanie.objects.get(id=task_a.id)
        assert task_b in updated_task_a.depends_on.all()

    def test_add_dependency_detects_cycle_simple(self, db, wielu_mistrz_user):
        task_a = Zadanie.objects.create(
            tytul="Task A",
            opis="A",
            warunki="A",
            assigned_to=wielu_mistrz_user,
        )
        task_b = Zadanie.objects.create(
            tytul="Task B",
            opis="B",
            warunki="B",
            assigned_to=wielu_mistrz_user,
        )
        task_a.depends_on.add(task_b)

        service = TodoService()

        with pytest.raises(Exception):
            service.add_dependency(task_b.id, task_a.id)

    def test_add_dependency_detects_cycle_chain(self, db, wielu_mistrz_user):
        task_a = Zadanie.objects.create(
            tytul="Task A",
            opis="A",
            warunki="A",
            assigned_to=wielu_mistrz_user,
        )
        task_b = Zadanie.objects.create(
            tytul="Task B",
            opis="B",
            warunki="B",
            assigned_to=wielu_mistrz_user,
        )
        task_c = Zadanie.objects.create(
            tytul="Task C",
            opis="C",
            warunki="C",
            assigned_to=wielu_mistrz_user,
        )
        task_a.depends_on.add(task_b)
        task_b.depends_on.add(task_c)

        service = TodoService()

        with pytest.raises(Exception):
            service.add_dependency(task_c.id, task_a.id)

    def test_add_dependency_multiple_valid(self, db, wielu_mistrz_user):
        task_a = Zadanie.objects.create(
            tytul="Task A",
            opis="A",
            warunki="A",
            assigned_to=wielu_mistrz_user,
        )
        task_b = Zadanie.objects.create(
            tytul="Task B",
            opis="B",
            warunki="B",
            assigned_to=wielu_mistrz_user,
        )
        task_c = Zadanie.objects.create(
            tytul="Task C",
            opis="C",
            warunki="C",
            assigned_to=wielu_mistrz_user,
        )

        service = TodoService()
        service.add_dependency(task_a.id, task_b.id)
        service.add_dependency(task_a.id, task_c.id)

        updated_task_a = Zadanie.objects.get(id=task_a.id)
        assert task_b in updated_task_a.depends_on.all()
        assert task_c in updated_task_a.depends_on.all()

    def test_add_dependency_returns_success_result(self, db, wielu_mistrz_user):
        task_a = Zadanie.objects.create(
            tytul="Task A",
            opis="A",
            warunki="A",
            assigned_to=wielu_mistrz_user,
        )
        task_b = Zadanie.objects.create(
            tytul="Task B",
            opis="B",
            warunki="B",
            assigned_to=wielu_mistrz_user,
        )

        service = TodoService()
        result = service.add_dependency(task_a.id, task_b.id)

        assert result is not None
        assert result.get("success") is True

    def test_get_task_raises_on_invalid_id(self, db):
        service = TodoService()

        with pytest.raises(Exception):
            service.get_task(999999)

    def test_complete_task_already_done(self, db, zadanie_done):
        service = TodoService()
        result = service.complete_task(zadanie_done.id)

        assert result.status == Status.DONE

    def test_get_tasks_filters_by_status(self, db, wielu_mistrz_user):
        Zadanie.objects.create(
            tytul="TODO Task",
            opis="Desc",
            warunki="Cond",
            status=Status.TODO,
            assigned_to=wielu_mistrz_user,
        )
        Zadanie.objects.create(
            tytul="DONE Task",
            opis="Desc",
            warunki="Cond",
            status=Status.DONE,
            assigned_to=wielu_mistrz_user,
        )

        service = TodoService()
        todo_tasks = service.get_tasks_by_status(Status.TODO)

        assert len(todo_tasks) == 1
        assert todo_tasks[0].status == Status.TODO

