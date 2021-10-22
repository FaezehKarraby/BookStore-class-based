from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('signup/', views.SignupView, name='signup'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('profile/new/', views.ProfileView, name='profile'),
]
