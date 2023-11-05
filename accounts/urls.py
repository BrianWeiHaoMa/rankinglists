from django.urls import path
from .views import SignUpView, CustomLoginView, SignUpSuccessView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("signup/success/", SignUpSuccessView.as_view(), name="signup-success"),
    path("login/", CustomLoginView.as_view(), name="login"),
]
