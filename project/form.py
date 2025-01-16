from django import forms
from django.contrib.auth.models import User
from project.models import UserProfile, Message
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password

class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = {"username", "password", "email"}

    def clean_password(self):
        password = self.cleaned_data.get("password")
        # Check the hashed password against all existing users
        for user in User.objects.all():
            if check_password(password, user.password):
                raise ValidationError("This password is already in use. Please choose a unique password.")
        return password

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = {"profile_name", "profile_last_name", "profile_department", "profile_age", "profile_pic"}

class Send_message(forms.ModelForm):
    class Meta:
        model = Message
        fields = {"content"}