from django.contrib import admin
from .views import Book, Category

admin.site.register(Book)
admin.site.register(Category)
