from rest_framework import serializers
from .models import Department,EmployeeProfile,Employee,Project

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ["id","name"]
class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ["id", "name", "department", "user"]

    def validate(self, data):
        name = data.get("name")
        department = data.get("department")

        if name and len(name.strip()) < 3:
            raise serializers.ValidationError(
                "Employee name must have at least 3 characters."
            )

        if department is None:
            raise serializers.ValidationError(
                "Department is required."
            )

        return data
class EmployeeProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeProfile
        fields = ["id","employee","phone"]
class EmployeeProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["name","employees"]