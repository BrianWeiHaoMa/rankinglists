from django.views.generic import (
    RedirectView,
    ListView,
    CreateView,
    DeleteView,
    UpdateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django_project.utils import (
    update_context_url_user,
    update_context_from_list, 
    update_url_user_views,
)
from list_items.models import ListItem
from .models import List
from .forms import ListForm


class ListsEntryView(LoginRequiredMixin, RedirectView):
    pattern_name = "lists"

    def get_redirect_url(self, *args, **kwargs):
        kwargs["user_pk"] = self.request.user.pk
        return super().get_redirect_url(*args, **kwargs)


class ListsView(UserPassesTestMixin, ListView):
    model = List
    template_name = "lists/lists.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.kwargs)
        update_context_url_user(context)
        update_url_user_views(context)
        return context

    def get_queryset(self):
        user = get_user_model().objects.get(pk=self.kwargs["user_pk"])
        if user == self.request.user:
            lists = super().get_queryset().filter(user=user)
        else:
            lists = super().get_queryset().filter(user=user, is_private=False)
        return lists.order_by("-views", "name")
        
    def test_func(self):
        user = get_user_model().objects.get(pk=self.kwargs["user_pk"])
        return user.is_active


class ListsCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    form_class = ListForm
    template_name = "lists/create.html"
    success_url = reverse_lazy("lists-entry")

    def form_valid(self, form):
        if len(List.objects.filter(name=form.instance.name, user=self.request.user)):
            form.add_error("name", "Another list with this name already exists.")
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.kwargs["user_pk"] == self.request.user.pk


class UserIsCreatorTestMixin(UserPassesTestMixin):
    def test_func(self):
        return self.get_object().user == self.request.user


class ListsUpdateView(LoginRequiredMixin, UserIsCreatorTestMixin, UpdateView):
    model = List
    form_class = ListForm
    template_name = "lists/update.html"
    success_url = reverse_lazy("lists-entry")


class ListsDeleteView(LoginRequiredMixin, UserIsCreatorTestMixin, DeleteView):
    model = List
    template_name = "lists/delete.html"
    success_url = reverse_lazy("lists-entry")


class ListsItemsView(UserPassesTestMixin, ListView):
    model = ListItem
    template_name = "lists/items.html"
    context_object_name = "list_item__list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.kwargs)
        update_context_url_user(context)
        update_url_user_views(context)
        update_context_from_list(context)
        return context

    def get_queryset(self):
        from_list = List.objects.get(pk=self.kwargs["list_pk"])
        from_list.views += 1
        from_list.save()
        return (
            super()
            .get_queryset()
            .filter(from_list=from_list)
            .order_by("-rating", "name")
        )

    def test_func(self):
        from_list = List.objects.get(pk=self.kwargs["list_pk"])
        url_user = get_user_model().objects.get(pk=self.kwargs["user_pk"])
        return (
            url_user.is_active and from_list.user == url_user and
            (from_list.user == self.request.user or not from_list.is_private)
        )
