from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from fashion_app.models import Profile, User


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('__all__')
        exclude = ('user',)


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')