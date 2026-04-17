import pytest
from dashboard.services import SearchService
from dashboard.models import Zadanie
from django.contrib.auth.models import User as DjangoUser


@pytest.mark.django_db
class TestSearchService:

    def test_search_by_email(self, db):
        user = DjangoUser.objects.create_user(
            username="testuser",
            email="john.doe@organization.com",
        )

        service = SearchService()
        results = service.search("john.doe@organization.com")

        assert len(results) > 0
        assert any(r.get("email") == "john.doe@organization.com" for r in results)

    def test_search_by_partial_email(self, db):
        DjangoUser.objects.create_user(
            username="user1",
            email="john.doe@organization.com",
        )
        DjangoUser.objects.create_user(
            username="user2",
            email="jane.smith@organization.com",
        )

        service = SearchService()
        results = service.search("john")

        assert len(results) > 0
        assert any("john" in r.get("email", "").lower() for r in results)

    def test_search_by_organization_name(self, db):
        DjangoUser.objects.create_user(
            username="user1",
            email="contact@acmecorp.com",
            first_name="ACME",
        )

        service = SearchService()
        results = service.search("ACME")

        assert len(results) > 0

    def test_search_case_insensitive(self, db):
        DjangoUser.objects.create_user(
            username="testuser",
            email="John.Doe@Organization.COM",
        )

        service = SearchService()
        results_lower = service.search("john.doe")
        results_upper = service.search("JOHN.DOE")

        assert len(results_lower) > 0
        assert len(results_upper) > 0

    def test_search_returns_aggregated_results(self, db):
        DjangoUser.objects.create_user(
            username="user1",
            email="search@example.com",
            first_name="SearchName",
        )

        service = SearchService()
        results = service.search("search")

        assert isinstance(results, list)
        assert len(results) > 0
        assert all(isinstance(r, dict) for r in results)

    def test_search_includes_user_data(self, db):
        user = DjangoUser.objects.create_user(
            username="testuser",
            email="contact@test.com",
            first_name="John",
            last_name="Doe",
        )

        service = SearchService()
        results = service.search("John Doe")

        assert len(results) > 0
        result = results[0]
        assert result.get("email") == "contact@test.com" or \
               result.get("name") == "John Doe" or \
               "John" in str(result)

    def test_search_empty_query(self, db):
        service = SearchService()
        results = service.search("")

        assert isinstance(results, list)

    def test_search_no_matches(self, db):
        DjangoUser.objects.create_user(
            username="testuser",
            email="test@example.com",
        )

        service = SearchService()
        results = service.search("nonexistent_search_term_xyz")

        assert isinstance(results, list)
        assert len(results) == 0

    def test_search_special_characters(self, db):
        DjangoUser.objects.create_user(
            username="testuser",
            email="user+tag@example.com",
        )

        service = SearchService()
        results = service.search("user+tag")

        assert len(results) > 0

    def test_search_returns_paginated_results(self, db):
        for i in range(20):
            DjangoUser.objects.create_user(
                username=f"user{i}",
                email=f"user{i}@example.com",
            )

        service = SearchService()
        results = service.search("user", limit=10)

        assert len(results) <= 10

    def test_search_full_text_on_email(self, db):
        DjangoUser.objects.create_user(
            username="user1",
            email="admin@searchcompany.com",
        )
        DjangoUser.objects.create_user(
            username="user2",
            email="support@otherdomain.com",
        )

        service = SearchService()
        results = service.search("searchcompany")

        assert len(results) > 0
        assert any("searchcompany" in r.get("email", "").lower() for r in results)

    def test_search_by_username(self, db):
        DjangoUser.objects.create_user(
            username="john_developer",
            email="john@dev.com",
        )

        service = SearchService()
        results = service.search("john_developer")

        assert len(results) > 0

    def test_search_performance_many_users(self, db):
        for i in range(100):
            DjangoUser.objects.create_user(
                username=f"searchuser{i}",
                email=f"searchuser{i}@company.com",
            )

        service = SearchService()
        results = service.search("searchuser", limit=50)

        assert len(results) > 0
        assert len(results) <= 50

    def test_search_includes_organization_data(self, db):
        user = DjangoUser.objects.create_user(
            username="orguser",
            email="admin@organization.pl",
            first_name="Admin",
        )

        service = SearchService()
        results = service.search("organization")

        assert len(results) > 0
        assert any(org_data.get("email") == "admin@organization.pl" for org_data in results)

