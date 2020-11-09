from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


class SignUpForm(UserCreationForm):
    last_name = forms.CharField(max_length=100, required=True, )

    class Meta:
        model = User
        fields = ('username', 'last_name', 'email', 'password1', 'password2', )
    

class UserLoginForm(forms.Form):
    '''
    this form use for login account
    '''
    username=forms.CharField()
    password= forms.CharField(widget=forms.PasswordInput)