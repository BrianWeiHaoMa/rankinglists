from django.forms import ModelForm
from .models import List


class ListForm(ModelForm):
    class Meta:
        model = List
        fields = (
            "name",
            "is_private",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs["placeholder"] = "Make this name unique."