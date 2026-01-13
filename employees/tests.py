import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import Employee
from datetime import date

@pytest.mark.django_db
def test_create_employee():
    user = User.objects.create_user(username="test", password="123")
    client = APIClient()
    client.force_authenticate(user=user)

    response = client.post("/api/employees/", {
        "name": "John",
        "email": "john@test.com",
        "phone": "9999999999",
        "department": "IT",
        "designation": "Developer",
        "salary": "50000",
        "date_of_joining": "2024-01-01",
        "is_active": True
    })

    assert response.status_code == 201
    assert Employee.objects.count() == 1


@pytest.mark.django_db
def test_get_employee():
    user = User.objects.create_user(username="test", password="123")
    emp = Employee.objects.create(
        name="Sam", email="sam@test.com", phone="111",
        department="HR", designation="Manager",
        salary=40000, date_of_joining=date.today()
    )

    client = APIClient()
    client.force_authenticate(user=user)
    response = client.get(f"/api/employees/{emp.id}/")

    assert response.status_code == 200
