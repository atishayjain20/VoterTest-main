from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MinValueValidator, MaxValueValidator

# this is for user which are developer not for the voter or general user
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        #fields = '__all__'
        fields = ['username',  'password1',
                   'password2','email']
        # exclude = ['contactno']


# class registrationTest(UserRegisterForm):
#     class Meta:
#         model = User
#         exclude = ['contactno']
