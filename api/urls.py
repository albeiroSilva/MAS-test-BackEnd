

from django.urls import path, include

from api import views

urlpatterns = [
    path(r'employees/<int:id>', views.employees),
    path(r'employees/', views.employees)
]