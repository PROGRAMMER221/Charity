from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignupForm(UserCreationForm):
    mobileno = forms.CharField(max_length=10)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'mobileno', 'password1', 'password2']
