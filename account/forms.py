from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label='نام', max_length=30, required=False, help_text='اختیاری')
    last_name = forms.CharField(label='نام خانوادگی', max_length=30, required=False, help_text='اختیاری')
    email = forms.EmailField(label='ایمیل', max_length=254, help_text='لطفا آدرس ایمیل معتبر وارد کنید')

    class Meta:
        model = User
        fields = [
        'username',
        'first_name',
        'last_name',
        'email',
        'password1',
        'password2'
        ]