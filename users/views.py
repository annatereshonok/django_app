from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.core.mail import send_mail
from django.contrib.auth import login

from .models import CustomUser
from .forms import CustomAuthenticationForm, CustomUserCreationForm


class CustomLoginView(LoginView):
    model = CustomUser
    form_class = CustomAuthenticationForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('catalog:catalog_list')


class CustomRegistrationView(FormView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('catalog:catalog_list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в наш сервис'
        message = 'Спасибо, что зарегистрировались в нашем сервисе!'
        from_email = 'anvtereshonok@gmail.com'
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)
