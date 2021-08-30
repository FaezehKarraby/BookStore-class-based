from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
    class Meta:
        verbose_name = 'نمایه کاربری'
        verbose_name_plural = 'نمایه کاربری'
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='حساب کاربری', null=True, blank=True, related_name='profile')
    mobile = models.CharField('تلفن همراه', max_length=11)

    gender_choices = (
    ('male', 'مرد'),
    ('female', 'زن'),
    )
    gender = models.IntegerField('جنسیت', choices=gender_choices, null=True, blank=True)

    birth_date = models.DateField('تاریخ تولد', null=True, blank=True)
    profile_image = models.ImageField('تصویر', upload_to='users/profile_images/', null=True, blank=True)
    balance = models.IntegerField('اعتبار', default=0)

    def __str__(self):
        return self.user.get_full_name()

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
