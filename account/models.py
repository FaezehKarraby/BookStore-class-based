from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='profile')
    mobile = models.CharField(max_length=11)

    gender_choices = (
        ('1', 'male'),
        ('2', 'female'),
    )
    gender = models.IntegerField(choices=gender_choices, null=True, blank=True)

    birth_date = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='users/profile_images/', null=True, blank=True)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return self.user.get_full_name()

    def get_absolute_url(self):
        return reverse('login')
