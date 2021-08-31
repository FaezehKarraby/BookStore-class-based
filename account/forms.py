from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from account.models import Profile
from django.core.exceptions import ValidationError


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label='نام', max_length=30, required=False, help_text='اختیاری')
    last_name = forms.CharField(label='نام خانوادگی', max_length=30, required=False, help_text='اختیاری')
    email = forms.EmailField(label='ایمیل', max_length=254, help_text='لطفا آدرس ایمیل معتبر وارد کنید')


    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2',]


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['mobile', 'gender', 'birth_date', 'balance', 'profile_image',]

    def save(self, user=None):
        user_profile = super(ProfileForm, self).save(commit=False)
        if user:
            user_profile.user = user
        user_profile.save()
        return user_profile
