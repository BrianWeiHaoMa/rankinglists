from django.views.generic import DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from django.contrib.auth import get_user_model
from django_project.utils import (
    update_context_url_user,
    update_context_from_list,
    update_url_user_views,
)
from lists.models import List
from .models import ListItem
from .forms import ListItemForm


class ListItemCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    form_class = ListItemForm
    template_name = "list_items/create.html"

    def get_success_url(self):
        return reverse("lists-items", kwargs=self.kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.kwargs)
        update_context_from_list(context)
        return context

    def form_valid(self, form):
        from_list = List.objects.get(pk=self.kwargs["list_pk"])
        if len(ListItem.objects.filter(name=form.instance.name, from_list=from_list)):
            form.add_error("name", "Another list item within the same list contains this name.")
        form.instance.from_list = from_list
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        url_user = get_user_model().objects.get(pk=self.kwargs["user_pk"])
        from_list = List.objects.get(pk=self.kwargs["list_pk"])
        return self.request.user == from_list.user == url_user
            

class ListItemDetailView(UserPassesTestMixin, DetailView):
    model = ListItem
    template_name = "list_items/detail.html"
    context_object_name = "list_item"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.kwargs)
        update_context_url_user(context)
        update_url_user_views(context)
        return context

    def test_func(self):
        url_user = get_user_model().objects.get(pk=self.kwargs["user_pk"])
        if not url_user.is_active:
            return False
        list_item = self.get_object()
        from_list = list_item.from_list
        if self.request.user != url_user:
            return not from_list.is_private and from_list.pk == self.kwargs["list_pk"]
        return (
            list_item.user == from_list.user == url_user and
            from_list.pk == self.kwargs["list_pk"]
        ) 


class UserIsCreatorTestMixin(UserPassesTestMixin):
    def test_func(self):
        user = get_user_model().objects.get(pk=self.kwargs["user_pk"])
        list_item = self.get_object()
        from_list = list_item.from_list
        return (
            self.request.user == list_item.user == from_list.user == user and
            self.kwargs["list_pk"] == from_list.pk
        )
    

class ListItemUpdateView(LoginRequiredMixin, UserIsCreatorTestMixin, UpdateView):
    model = ListItem
    form_class = ListItemForm
    template_name = "list_items/update.html"
    context_object_name = "list_item"

    def get_success_url(self):
        return reverse("list-items-detail", kwargs=self.kwargs)


class ListItemDeleteView(LoginRequiredMixin, UserIsCreatorTestMixin, DeleteView):
    model = ListItem
    template_name = "list_items/delete.html"
    context_object_name = "list_item"

    def get_success_url(self):
        self.kwargs.pop("pk")
        return reverse("lists-items", kwargs=self.kwargs)
