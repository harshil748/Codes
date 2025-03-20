from django.urls import path
from . import views

urlpatterns = [
    path("", views.calculator, name="calculator"),
]
# Compare this snippet from calculator_project/calculator/views.py: