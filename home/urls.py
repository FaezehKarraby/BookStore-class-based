from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('search/', views.search, name='search'),
]
