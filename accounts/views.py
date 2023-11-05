from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from verify_email.email_handler import send_verification_email
from .forms import CustomUserCreationForm, CustomLoginForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("signup-success")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        inactive_user = send_verification_email(self.request, form)
        return HttpResponseRedirect(self.success_url)


class SignUpSuccessView(TemplateView):
    template_name = "registration/email_verification/new_email_sent.html"


class CustomLoginView(LoginView):
    form_class = CustomLoginForm