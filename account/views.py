from django.contrib.auth.decorators import login_required
from account.forms import SignUpForm, ProfileForm, LoginForm, EditProfileForm, UpdateProfileForm
from account.models import Profile
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse


def SignupView(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=password)
                login(request, user)
                return render(request, 'home.html')
        else:
            form = SignUpForm()
        return render(request, 'account/signup.html', {'form': form})
    else:
        return HttpResponseRedirect(reverse('home:home'))


def LoginView(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
                if user:
                    context = {
                        'form': form,
                        'user': user,
                    }
                    login(request, user=user)
                    if request.GET.get('next'):
                        return HttpResponseRedirect(request.GET['next'])
                    return render(request, 'home.html', context)
                else:
                    context = {
                        'form': form,
                        'error': 'username or password is wrong...!',
                    }
            else:
                context = {
                    'form': form,
                }
        else:
            form = LoginForm()
            context = {
                'form': form,
            }
        return render(request, 'account/login.html', context)
    else:
        return HttpResponseRedirect(reverse('home:home'))


def LogoutView(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect(reverse('account:login'))
    return HttpResponseRedirect('home:home')


@login_required
def ProfileView(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            context = {
                'boldmessage': 'I am bold font from the context',
            }
            return render(request, 'home:home.html', context)
        else:
            print(form.errors)
    else:
        form = ProfileForm()
    return render(request, 'account/profile.html', {'form': form})
