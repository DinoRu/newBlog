from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm
from django.contrib.auth.views import PasswordChangeView


class UserRegisterView(generic.CreateView):

    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditProfileView(generic.UpdateView):

    form_class = EditProfileForm
    template_name = 'registration/edit_profil.html'
    success_url = reverse_lazy('login')

    def get_object(self):
        return self.request.user


class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('members:password_success')


def password_success(request):
    return render(request, 'registration/password_success.html', {})