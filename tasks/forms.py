from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Task

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):


    class Meta:
        model = User
        fields = ['username', 'password']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['owner']