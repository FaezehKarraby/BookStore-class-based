from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    class Meta:
        verbose_name = 'نمایه کاربری'
        verbose_name_plural = 'نمایه کاربری'
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='حساب کاربری')
    mobile = models.CharField('تلفن همراه', max_length=11)

    gender_choices = (
    ('male', 'مرد'),
    ('female', "زن"),
    )
    gender = models.IntegerField('جنسیت', choices=gender_choices, null=True, blank=True)

    birth_date = models.DateField('تاریخ تولد', null=True, blank=True)
    profile_image = models.ImageField('تصویر', upload_to='users/profile_images/', null=True, blank=True)
    balance = models.IntegerField('اعتبار', default=0)

    def __str__(self):
        return self.user.get_full_name()

    def __unicode__(self):
        return u'%s' % self.user
