from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def login_view(request):
    next_url = request.GET.get('next')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            redirect_url = next_url if next_url else reverse('product:category_list')
            return HttpResponseRedirect(redirect_url)
        else:
            context = {
            'username': username,
            'error': 'کاربری با این مشخصات یافت نشد',
            }
    else:
        context = {}
    return render(request, 'account/login.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('account:login'))

@login_required
def profile_detail(request):
    profile = request.user.profile
    context = {
    'profile': profile
    }
    return render(request, 'account/profile_detail.html', context)
