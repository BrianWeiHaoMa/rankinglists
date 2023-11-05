from django.db import models
from django.contrib.auth import get_user_model
from lists.models import List


class ListItem(models.Model):
    name = models.CharField(verbose_name="Item name", max_length=128, blank=False)
    rating = models.FloatField("Item rating")
    description = models.TextField("Item description", max_length=8192, blank=True)
    from_list = models.ForeignKey(List, on_delete=models.CASCADE)
    date_created = models.DateTimeField("Date created", auto_now_add=True)
    date_last_modified = models.DateTimeField("Date last modified", auto_now=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.rating = round(min(max(self.rating, 0), 10), 3)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} --({self.from_list.name})-({self.from_list.user.username})"
