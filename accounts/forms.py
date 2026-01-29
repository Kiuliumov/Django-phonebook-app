from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Account
from django.core.validators import RegexValidator


class RegistrationForm(UserCreationForm):

    username = forms.CharField(
        label='Username',
        validators=[RegexValidator(regex=r'^[A-Za-z0-9]+$')],
    )
    email = forms.EmailField()

    class Meta:
        model = Account
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):

    username = forms.CharField(
        label="Username or Email",
        widget=forms.TextInput(attrs={
            "autofocus": True,
            "placeholder": "Username or email"
        })
    )

