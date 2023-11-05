from django.urls import path, include
from .views import (
    ListsEntryView,
    ListsView,
    ListsCreateView,
    ListsUpdateView,
    ListsDeleteView,
    ListsItemsView,
)

urlpatterns = [
    path("", ListsEntryView.as_view(), name="lists-entry"),
    path("<int:user_pk>/", ListsView.as_view(), name="lists"),
    path("<int:user_pk>/create/", ListsCreateView.as_view(), name="lists-create"),
    path("<int:user_pk>/update/<int:pk>/", ListsUpdateView.as_view(), name="lists-update"),
    path("<int:user_pk>/delete/<int:pk>/", ListsDeleteView.as_view(), name="lists-delete"),
    path("<int:user_pk>/list/<int:list_pk>/", ListsItemsView.as_view(), name="lists-items"),
    path("<int:user_pk>/list/<int:list_pk>/item/", include("list_items.urls")),
]