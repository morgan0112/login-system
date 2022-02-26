from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy, reverse
from .forms import RegisterForm, ChangePasswordForm, LoginForm, UserProfileForm
from django.contrib.auth import login, logout
from django.contrib.auth import views as auth_views
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import LoginLog


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            LoginLog.objects.create(user=user)
            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})


class LoginPageView(generic.FormView):
    form_class = LoginForm
    template_name = "accounts/login.html"

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        LoginLog.objects.create(user=user)
        return super(LoginPageView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Username or Password is invalid")
        return super().form_valid(form)

    def get_success_url(self):
        if self.request.method == 'POST':
            form = LoginForm(data=self.request.POST)
            if form.is_valid():
                if 'next' in self.request.POST:
                    return reverse(self.request.POST.get('next')[1:-1])
                else:
                    return reverse('home')
            else:
                return reverse('accounts:login')


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


class UserEditProfileForm(SuccessMessageMixin, generic.UpdateView):
    form_class = UserProfileForm
    template_name = 'accounts/edit_profile.html'
    success_url = reverse_lazy('accounts:account')
    success_message = "Account has been successfully updated"

    def get_object(self, queryset=None):
        return self.request.user


class PasswordsChangeView(auth_views.PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = 'accounts/change-password.html'
    success_url = reverse_lazy('accounts:password_success')


class PasswordSuccessView(generic.TemplateView):
    template_name = 'accounts/password-success.html'
