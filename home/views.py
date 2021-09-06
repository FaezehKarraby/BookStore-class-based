from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from product.models import Book

class HomePageView(TemplateView):
    template_name = 'home.html'


class SearchResultView(ListView):
    model = Book
    template_name = 'home/search_results.html'

    def get_queryset(self):
        if 'q' in self.request.GET:
            query = self.request.GET.get('q')
            if not query:
                query = 'None'
            object_list = Book.objects.filter(Q(title__contains=query))
            return object_list
        else:
            error='یافت نشد'

def search(request):
    error = ''
    query = ''
    books1 = ''
    books2 = ''
    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            query = 'None'
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
    return render(request, 'home/search.html', context)
