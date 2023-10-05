import random

from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LoginView as BaseLogoutView
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.conf import settings
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class LoginView(BaseLoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('mainapp:breeds')


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        new_user = form.save()
        send_mail(
            subject='Поздравляем с регистрацией',
            message='Вы зарегистрировались на нашей платформе. Добро пожаловать!',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]

        )
        return super().form_valid(form)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
    send_mail(
        subject='Вы сменили пароль',
        message=f'Ваш новый пароль {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('mainapp:popular_list'))