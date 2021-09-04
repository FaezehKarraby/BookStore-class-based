from django.views.generic import CreateView, UpdateView, FormView, DeleteView
from account.forms import SignUpForm, ProfileForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from account.models import Profile
from django.contrib.auth import get_user_model
from django.http import HttpResponse, HttpResponseRedirect



class SignUpView(CreateView):
    model = Profile
    form_class = SignUpForm
    #fields = ['user', 'mobile', 'gender', 'birth_date', 'profile_image', 'balance']
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class ProfileView(CreateView):
    form_class = ProfileForm
    model = Profile
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
    model = User
    success_url = reverse_lazy('account:all_accounts')
    template_name = 'account/user_confirm_delete.html'


def get_all_users(request):
    users = User.objects.all()
    context = {
    'users': users[1:],
    }
    return render(request, 'account/all_accounts.html', context)


def get_detail_view(request, pk):
    user = User.objects.get(id=pk)
    context = {
    'user': user,
    }
    return render(request, 'account/account_detail.html', context)


def exit(request):
    context = {
    }
    return render(request, 'account/exit.html', context)
