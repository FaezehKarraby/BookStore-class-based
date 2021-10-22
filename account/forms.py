from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from account.models import Profile
from django.core.exceptions import ValidationError


class SignUpForm(UserCreationForm):
    pass


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['mobile', 'gender', 'birth_date', 'balance', 'profile_image', ]


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'username',
            'email',
        )
        exclude = ('password',)


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'mobile',
            'balance',
        )
        exclude = ('user',)
