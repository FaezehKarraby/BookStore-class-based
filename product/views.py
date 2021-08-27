from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Book, Category


class CategoryListView(ListView):
    model = Category

class BookListView(ListView):
    model = Book

class BookDetailView(DetailView):
    model = Book
