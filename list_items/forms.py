from django.forms import ModelForm
from .models import ListItem


class ListItemForm(ModelForm):
    class Meta:
        model = ListItem
        fields = (
            "name",
            "rating",
            "description",
        )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs["placeholder"] = "Make this name unique."
        self.fields["rating"].widget.attrs["placeholder"] = "0.000-10.000."