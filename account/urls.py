from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/detail/', views.profile_detail, name='profile_detail'),
]
