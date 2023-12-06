from .models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'username', 'password1', 'password2']