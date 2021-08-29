from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from account.models import Profile


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label='نام', max_length=30, required=False, help_text='اختیاری')
    last_name = forms.CharField(label='نام خانوادگی', max_length=30, required=False, help_text='اختیاری')
    email = forms.EmailField(label='ایمیل', max_length=254, help_text='لطفا آدرس ایمیل معتبر وارد کنید')
    mobile = forms.CharField(label='تلفن همراه', max_length=14, help_text='98+')
    #birth_date = forms.DateField(label='تاریخ تولد')

    gender_choices = (
    ('male', 'مرد'),
    ('female', "زن"),
    )
    gender = forms.ChoiceField(label='جنسیت', choices=gender_choices)

    class Meta:
        model = User
        fields = [
        'username',
        'first_name',
        'last_name',
        'email',
        'password1',
        'password2',

        ]

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = [
        'mobile',
        'gender',
        'birth_date',
        'balance',
        'profile_image',

        ]

    def save(self, user=None):
        user_profile = super(ProfileForm, self).save(commit=False)
        if user:
            user_profile.user = user
        user_profile.save()
        return user_profile
