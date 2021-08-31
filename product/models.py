from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField('عنوان', max_length=10)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('product:category_list')


class Book(models.Model):
    class Meta:
        verbose_name = 'کتاب'
        verbose_name_plural = 'کتاب ها'
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField('عنوان', max_length=100)
    author = models.CharField('نویسنده', max_length=100)
    inventory = models.PositiveIntegerField('موجودی')
    price = models.DecimalField('قیمت', max_digits=20, decimal_places=5)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='دسته بندی')


    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('product:book_list')
