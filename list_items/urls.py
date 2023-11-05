from django.urls import path
from .views import (
    ListItemDetailView,
    ListItemCreateView,
    ListItemDeleteView,
    ListItemUpdateView,
)

urlpatterns = [
    path("create/", ListItemCreateView.as_view(), name="list-items-create"),
    path("<int:pk>/detail/", ListItemDetailView.as_view(), name="list-items-detail"),
    path("<int:pk>/delete/", ListItemDeleteView.as_view(), name="list-items-delete"),
    path("<int:pk>/update/", ListItemUpdateView.as_view(), name="list-items-update"),
]
