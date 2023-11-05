from django.urls import path
from .views import UsersListView

urlpatterns = [
    path("users/", UsersListView.as_view(), name="users"),
]