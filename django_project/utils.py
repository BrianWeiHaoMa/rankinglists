from django.contrib.auth import get_user_model
from lists.models import List

def update_context_url_user(context):
    url_user = get_user_model().objects.get(pk=context["user_pk"])
    context["url_user"] = url_user

# Should be placed after update_context_url_user.
def update_url_user_views(context):
    url_user = context["url_user"]
    url_user.views += 1
    url_user.save()

def update_context_from_list(context):
    from_list = List.objects.get(pk=context["list_pk"])
    context["from_list"] = from_list
