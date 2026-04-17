import pytest
from django.core.exceptions import ValidationError
from dashboard.models import Zadanie, Status


@pytest.mark.django_db
class TestZadanieModel:
    def test_zadanie_create_with_required_fields(self, wielu_mistrz_user):
        zadanie = Zadanie.objects.create(
            tytul="Test Task",
            opis="Test description",
            warunki="Test conditions",
            status=Status.TODO,
            assigned_to=wielu_mistrz_user,
        )
        assert zadanie.id is not None
        assert zadanie.tytul == "Test Task"
        assert zadanie.opis == "Test description"
        assert zadanie.warunki == "Test conditions"
        assert zadanie.status == Status.TODO
        assert zadanie.assigned_to == wielu_mistrz_user

    def test_zadanie_default_status_is_todo(self, wielu_mistrz_user):
        zadanie = Zadanie.objects.create(
            tytul="Test Task",
            opis="Description",
            warunki="Conditions",
            assigned_to=wielu_mistrz_user,
        )
        assert zadanie.status == Status.TODO

    def test_zadanie_created_at_is_set_automatically(self, wielu_mistrz_user):
        zadanie = Zadanie.objects.create(
            tytul="Test Task",
            opis="Description",
            warunki="Conditions",
            assigned_to=wielu_mistrz_user,
        )
        assert zadanie.created_at is not None

    def test_zadanie_completed_at_is_none_initially(self, wielu_mistrz_user):
        zadanie = Zadanie.objects.create(
            tytul="Test Task",
            opis="Description",
            warunki="Conditions",
            assigned_to=wielu_mistrz_user,
        )
        assert zadanie.completed_at is None

    def test_zadanie_can_have_dependencies(self, wielu_mistrz_user):
        zadanie_a = Zadanie.objects.create(
            tytul="Task A",
            opis="Description A",
            warunki="Conditions A",
            assigned_to=wielu_mistrz_user,
        )
        zadanie_b = Zadanie.objects.create(
            tytul="Task B",
            opis="Description B",
            warunki="Conditions B",
            assigned_to=wielu_mistrz_user,
        )
        zadanie_a.depends_on.add(zadanie_b)

        assert zadanie_b in zadanie_a.depends_on.all()

    def test_zadanie_dependencies_multiple(self, wielu_mistrz_user):
        zadanie_main = Zadanie.objects.create(
            tytul="Main Task",
            opis="Main",
            warunki="Main",
            assigned_to=wielu_mistrz_user,
        )
        dep1 = Zadanie.objects.create(
            tytul="Dependency 1",
            opis="Dep 1",
            warunki="Dep 1",
            assigned_to=wielu_mistrz_user,
        )
        dep2 = Zadanie.objects.create(
            tytul="Dependency 2",
            opis="Dep 2",
            warunki="Dep 2",
            assigned_to=wielu_mistrz_user,
        )
        zadanie_main.depends_on.add(dep1, dep2)

        assert dep1 in zadanie_main.depends_on.all()
        assert dep2 in zadanie_main.depends_on.all()
        assert zadanie_main.depends_on.count() == 2

    def test_zadanie_change_status_to_done(self, zadanie_todo):
        zadanie_todo.status = Status.DONE
        zadanie_todo.save()

        assert zadanie_todo.status == Status.DONE

    def test_zadanie_completed_at_set_when_status_done(self, zadanie_todo):
        import datetime
        before = datetime.datetime.now()
        zadanie_todo.status = Status.DONE
        zadanie_todo.completed_at = datetime.datetime.now()
        zadanie_todo.save()
        after = datetime.datetime.now()

        assert zadanie_todo.completed_at is not None
        assert before <= zadanie_todo.completed_at <= after

    def test_zadanie_unassigned_can_be_created(self, db):
        zadanie = Zadanie.objects.create(
            tytul="Unassigned Task",
            opis="No assignment",
            warunki="Conditions",
        )
        assert zadanie.assigned_to is None

    def test_zadanie_multiple_users_can_be_assigned(self, db):
        user1 = DjangoUser.objects.create_user(username="user1", email="user1@test.com")
        user2 = DjangoUser.objects.create_user(username="user2", email="user2@test.com")

        zadanie1 = Zadanie.objects.create(
            tytul="Task for User1",
            opis="Desc",
            warunki="Cond",
            assigned_to=user1,
        )
        zadanie2 = Zadanie.objects.create(
            tytul="Task for User2",
            opis="Desc",
            warunki="Cond",
            assigned_to=user2,
        )

        assert zadanie1.assigned_to == user1
        assert zadanie2.assigned_to == user2


@pytest.mark.django_db
class TestUserModel:
    def test_user_has_email(self, wielu_mistrz_user):
        assert wielu_mistrz_user.email == "mistrz@org.pl"

    def test_user_has_name(self, wielu_mistrz_user):
        assert wielu_mistrz_user.username == "wielu_mistrz"

    def test_user_can_have_multiple_assigned_tasks(self, wielu_mistrz_user):
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

        tasks = Zadanie.objects.filter(assigned_to=wielu_mistrz_user)
        assert tasks.count() == 2

