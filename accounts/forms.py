from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from accounts.models import User
from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'phone_number', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')


