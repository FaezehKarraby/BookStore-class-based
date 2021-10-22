from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('book/list/', views.BookListView, name='book_list'),
]
