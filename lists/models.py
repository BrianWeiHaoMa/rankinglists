from django.db import models
from django.contrib.auth import get_user_model


class List(models.Model):
    name = models.CharField(verbose_name="List name", max_length=128, blank=False)
    is_private = models.BooleanField("Private status", default=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    views = models.PositiveIntegerField("List views count", default=0)

    def __str__(self):
        return f"{self.name} -({self.user.username})"
