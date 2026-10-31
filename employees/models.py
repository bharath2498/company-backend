from django.db import models
from django.conf import settings

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    name = models.CharField(max_length=100)

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
class EmployeeProfile(models.Model):
    employee = models.OneToOneField(Employee,on_delete =models.CASCADE)
    phone = models.CharField(max_length=15)
    def __str__(self):
            return self.employee.name
class Project(models.Model):
    name = models.CharField(max_length=100)
    employees = models.ManyToManyField(Employee)
    def __str__(self):
                return self.name
