from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from .models import *


class MyForm(UserCreationForm):
    class Meta:
        model = User
        #fields = '__all__'
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class DropForm(forms.ModelForm):
    class Meta:
        model = CHILD1
        fields = ['Select']