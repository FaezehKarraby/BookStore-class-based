from django import forms
from .models import Book, Category
from django.core.exceptions import ValidationError


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(CategoryCreateForm, self).__init__(*args, **kwargs)

    def clean_title(self):
        title = self.cleaned_data['title']
        if Category.objects.filter(title=title).exists():
            raise forms.ValidationError('این دسته بندی موجود است.')
        return title


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(BookCreateForm, self).__init__(*args, **kwargs)

    def clean_title(self):
        title = self.cleaned_data['title']
        if Book.objects.filter(title=title).exists():
            raise forms.ValidationError("این نام کتاب موجود است.")
        return title
