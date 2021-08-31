from django.views.generic import CreateView, UpdateView, FormView, DeleteView
from account.forms import SignUpForm, ProfileForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from account.models import Profile


class SignUpView(CreateView):
    model = Profile
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class ProfileView(FormView):
    form_class = ProfileForm
    template_name = 'registration/profile.html'

    def form_valid(self, form):
        form.save(self.request.user)
        return super(ProfileView, self).form_valid(form)

    def get_success_url(self, *args, **kwargs):
        return reverse('login')


class ProfileEdit(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'registration/profile_edit.html'

    def get_object(self, *args, **kwargs):
        user = get_object_or_404(User, pk=self.kwargs['pk'])


    def get_success_url(self, *args, **kwargs):
        return reverse('profile')


class ProfileDeleteView(DeleteView):
    model = Profile
    success_url = reverse_lazy('logout')
