from django import forms
from django.forms import ModelForm
from . models import UserProfile





class CreateUserProfile(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['profile_id', 'user']


class UpdateUserProfile(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']




