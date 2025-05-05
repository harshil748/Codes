from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("signup/", views.signup, name="signup"),
    path("admin-dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("client-dashboard/", views.client_dashboard, name="client_dashboard"),
    path("add-book/", views.add_book, name="add_book"),
    path("edit-book/<int:pk>/", views.edit_book, name="edit_book"),
    path("delete-book/<int:pk>/", views.delete_book, name="delete_book"),
    path("borrow-book/<int:pk>/", views.borrow_book, name="borrow_book"),
    path("return-book/", views.return_book, name="return_book"),
]
