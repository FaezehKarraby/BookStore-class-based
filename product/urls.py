from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('', views.CategoryListView.as_view(), name='category_list'),
    path('create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),

    path('books/', views.BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('books/create/', views.BookCreateView.as_view(), name='book_create'),
    path('<int:pk>/books/update/', views.BookUpdateView.as_view(), name='book_update'),
    path('<int:pk>/books/delete/index.html', views.BookDeleteView.as_view(), name='book_delete'),
    path('shop/', views.book_shop, name='book_shop'),
]
