from django.shortcuts import render


def BookListView(request):
    return render(request, 'product/books_list.html')
