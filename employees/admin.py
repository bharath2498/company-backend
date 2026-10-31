from django.contrib import admin
from .models import Department, Employee, EmployeeProfile, Project


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "department"]
    search_fields = ["name"]
    list_filter = ["department"]


@admin.register(EmployeeProfile)
class EmployeeProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "employee", "phone"]
    search_fields = ["employee__name", "phone"]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]