from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, UsernameField
from django.forms import TextInput
from django.core.exceptions import ValidationError
from .models import CustomUser
from captcha.fields import ReCaptchaField


class CustomUserCreationForm(UserCreationForm):
    # captcha = ReCaptchaField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].required = True

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )


class CustomUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].required = True

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
        )


class CustomLoginForm(AuthenticationForm):
    # captcha = ReCaptchaField()
    # username = UsernameField(widget=TextInput(attrs={"autofocus": True}), label="Email")
    # def get_invalid_login_error(self):
    #     return ValidationError(
    #         self.error_messages["invalid_login"],
    #         code="invalid_login",
    #         params={"username": "email"},
    #     )
    pass