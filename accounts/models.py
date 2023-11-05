from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    email = models.EmailField(_("Email"), blank=True, unique=True)
    views = models.PositiveIntegerField("User views count", default=0)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
