from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('', views.CategoryListView.as_view(), name='category_list'),
    path('books/', views.BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
]
