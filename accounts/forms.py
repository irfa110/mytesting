from cProfile import label
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User
from django import forms

class CustomUserCreationForm(forms.Form):
    email = forms.EmailField(label="Email")
    phone = forms.IntegerField(label="Phone")
    password = forms.CharField(widget=forms.PasswordInput,label="password")
    conformpassword = forms.CharField(widget=forms.PasswordInput,label="conform password")


    # class Meta:
    #     model = User
    #     fields = ('email','password','phone')

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput,label="password")


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = "__all__"