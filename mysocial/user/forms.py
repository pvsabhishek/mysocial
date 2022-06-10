from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Profile

class SignUpForm(UserCreationForm):
	name = forms.CharField(label = ("Full Name"))
	username = forms.EmailField(label = ("Email"))
	phonenumber = forms.CharField(max_length=12, label=("phone"))

	class Meta:
		model = User
		fields = ('name', 'username', 'phonenumber' , 'password1', 'password2')

