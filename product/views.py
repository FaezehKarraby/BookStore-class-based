from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView
from .models import Book, Category
from django.http import HttpResponseRedirect
from .forms import BookCreateForm, CategoryCreateForm

class CategoryListView(ListView):
    model = Category


class BookListView(ListView):
    model = Book


class BookDetailView(DetailView):
    model = Book


class CategoryCreateView(CreateView):
    template_name = 'product/category_create.html'
    form_class = CategoryCreateForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_initial(self, *args, **kwargs):
        initial = super(CategoryCreateView, self).get_initial(**kwargs)
        initial['title'] = 'My Title'
        return initial

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CategoryCreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs


class BookCreateView(CreateView):
    template_name = 'product/book_create.html'
    form_class = BookCreateForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_initial(self, *args, **kwargs):
        initial = super(BookCreateView, self).get_initial(**kwargs)
        initial['title'] = 'My Title'
        return initial

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(BookCreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs
