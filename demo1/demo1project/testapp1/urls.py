from django.urls import path
from testapp1 import views

urlpatterns = [
    path('emp/', views.employee_detail),
]