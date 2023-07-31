from django.contrib.auth.forms import UserCreationForm
from accounts.models import User


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name' , 'last_name', 'phone_number', 'password1', 'password2')
