from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Q
from product.models import Book

class HomePageView(TemplateView):
    template_name = 'home/home_page.html'

def search(request):
    error = ''
    query = ''
    books1 = ''
    books2 = ''
    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            error = 'لطفا مقدار صحیحی وارد کنید'
        else:
            books1 = Book.objects.filter(Q(title__contains=query))
            books2 = Book.objects.filter(Q(author__contains=query))
    else:
        error = 'درخواست مورد نظر یافت نشد'
    context = {
    'error': error,
    'query': query,
    'books1': books1,
    'books2': books2,
    }
    return render(request, 'home/search_results.html', context)
