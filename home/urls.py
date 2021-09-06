from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('search/', views.search, name='search'),
    path('search/advanced/', views.SearchResultView.as_view(), name='search_advanced'),
]
