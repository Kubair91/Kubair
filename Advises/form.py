from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class signupForm(UserCreationForm):
    first_name=forms.CharField(help_text="Enter Your First Name")
    last_name=forms.CharField(help_text="Enter Your Last Name")
    email=forms.EmailField(help_text="Enter Your Email ID")
    #Age=forms.DateTimeField(help_text="Enter Your Age")
    class Meta:
        model=User
        fields=['username',
                'first_name',
                'last_name',
                'email',
                'password1',
                'password2',
                ]


