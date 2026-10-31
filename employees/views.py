from rest_framework import viewsets,filters
import logging

from .models import Department, Employee, EmployeeProfile,Project
from .serializers import (
    DepartmentSerializer,
    EmployeeSerializer,
    EmployeeProfileSerializer,
    EmployeeProjectSerializer
)
from .permissions import IsEmployeeOwner
from rest_framework.permissions import IsAuthenticated

logger = logging.getLogger(__name__)


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    filter_backends = [filters.OrderingFilter]

    ordering_fields = ["name", "id"]
    def get_queryset(self):
        logger.info(
    f"Employee list requested by user {self.request.user}"
)
        return Employee.objects.filter(
            user=self.request.user
        ).order_by("id")
    permission_classes = [IsEmployeeOwner,IsAuthenticated]

class EmployeeProfileViewSet(viewsets.ModelViewSet):
    queryset = EmployeeProfile.objects.all()
    serializer_class = EmployeeProfileSerializer
class EmployeeProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = EmployeeProjectSerializer