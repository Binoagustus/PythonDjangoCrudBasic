from django.urls import path
from .views import EmployeeViewSet

urlpatterns = [
    path('employee/', EmployeeViewSet.as_view()),
    path('employee/<int:id>', EmployeeViewSet.as_view())
]