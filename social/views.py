from django.views.generic import ListView
from django.contrib.auth import get_user_model


class UsersListView(ListView):
    model = get_user_model()
    template_name = "social/users.html"
    context_object_name = "user_list"

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(is_active=True)
            .order_by("-views", "username")
        )