from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, EmployeeViewSet,EmployeeProfileViewSet,EmployeeProjectViewSet


router = DefaultRouter()

router.register(
    "departments",
    DepartmentViewSet,
    basename="department"
)

router.register(
    "employees",
    EmployeeViewSet,
    basename="employee"
)

router.register(
    "employeeProfiles",
    EmployeeProfileViewSet,
    basename="employeeProfile"
)

router.register(
    "employeeProjects",
    EmployeeProjectViewSet,
    basename="employeeProject"
)


urlpatterns = router.urls