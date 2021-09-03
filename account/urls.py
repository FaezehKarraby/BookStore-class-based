from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),

    path('profile/new/', views.ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/edit/', views.ProfileEdit.as_view(), name='profileedit'),
    path('profile/all/', views.get_all_users, name='all_accounts'),
    path('profile/detail/<int:pk>/', views.get_detail_view, name='account_detail'),
    path('<int:pk>/profile/delete/index.html', views.ProfileDeleteView.as_view(), name='delete'),

    path('exit/', views.exit, name='exit'),
]
