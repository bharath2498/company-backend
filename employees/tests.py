from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from .models import Department, Employee


User = get_user_model()


class EmployeeAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="test12345"
        )

        self.department = Department.objects.create(
            name="IT"
        )

        self.employee = Employee.objects.create(
            name="Bharath",
            department=self.department,
            user=self.user
        )

        self.client.force_authenticate(user=self.user)
    def test_employee_list(self):
        response = self.client.get("/api/employees/")

        self.assertEqual(response.status_code, 200)
    def test_create_employee(self):
        second_user = User.objects.create_user(
            username="ravi",
            password="test12345"
        )

        data = {
            "name": "Ravi",
            "department": self.department.id,
            "user": second_user.id
        }

        response = self.client.post(
            "/api/employees/",
            data,
            format="json"
        )

        self.assertEqual(response.status_code, 201)
    def test_employee_name_validation(self):
        second_user = User.objects.create_user(
            username="shortnameuser",
            password="test12345"
        )

        data = {
            "name": "A",
            "department": self.department.id,
            "user": second_user.id
        }

        response = self.client.post(
            "/api/employees/",
            data,
            format="json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn(
        "Employee name must have at least 3 characters.",
        str(response.data)
    )
    def test_employee_list_requires_authentication(self):
        self.client.force_authenticate(user=None)

        response = self.client.get("/api/employees/")

        self.assertEqual(response.status_code, 401)
    def test_user_cannot_access_another_employee(self):
        second_user = User.objects.create_user(
            username="ravi",
            password="test12345"
        )

        second_employee = Employee.objects.create(
            name="Ravi",
            department=self.department,
            user=second_user
        )

        response = self.client.get(
            f"/api/employees/{second_employee.id}/"
        )

        self.assertEqual(response.status_code, 404)
    def test_employee_list_with_jwt(self):
        self.client.force_authenticate(user=None)

        token_response = self.client.post(
            "/api/token/",
            {
                "username": "testuser",
                "password": "test12345"
            },
            format="json"
        )

        self.assertEqual(token_response.status_code, 200)

        access_token = token_response.data["access"]

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {access_token}"
        )

        response = self.client.get("/api/employees/")

        self.assertEqual(response.status_code, 200)
