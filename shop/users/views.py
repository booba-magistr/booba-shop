from django.contrib import auth
from django.contrib.auth import get_user_model
from django.db.models.base import Model as Model
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, UpdateView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin

from carts.models import Carts
from .forms import (
    LoginUserForm,
    ProfileUserForm,
    RegisterUserForm,
    UserPasswordChangeForm,
)

# Create your views here.
class RegistrationUser(CreateView):
    form_class = RegisterUserForm
    template_name = "users/registration.html"
    success_url = reverse_lazy("user:login")
    extra_context = {'title': 'Регистрация'}


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "users/login.html"
    extra_context = {'title': 'Вход'}

    def get_success_url(self):
        redirect_page = self.request.POST.get('next', None)
        if redirect_page and redirect_page != reverse('user:logout'):
            return redirect_page
        return reverse_lazy('home')
    
    def form_valid(self, form):
        session_key = self.request.session.session_key
        user = form.get_user()
        if user: 
            auth.login(self.request, user)
            if session_key:
                forgot_carts = Carts.objects.filter(user=user)
                if forgot_carts.exists():
                    forgot_carts.delete()
                Carts.objects.filter(session_key=session_key).update(user=user)
                return HttpResponseRedirect(self.get_success_url())
        return HttpResponseRedirect(self.get_success_url())



class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = "users/profile.html"
    extra_context = {"title": "Профиль"}
    context_object_name = "orders"

    def get_success_url(self):
        return reverse_lazy("home")

    def get_object(self, queryset=None):
        return self.request.user


class UserPasswordChange(PasswordChangeView):
    template_name = "users/password_change_form.html"
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("user:password_change_done")


class UserCart(TemplateView):
    template_name = "users/user-cart.html"
    extra_context = {"title": "Корзина"}
