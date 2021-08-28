from django.views.generic import CreateView
from account.forms import SignUpForm
from django.urls import reverse_lazy
from django.shortcuts import render

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
