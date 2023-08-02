from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from goods_map.forms import LoginForm


class HomeView(LoginRequiredMixin, View):

    def get(self, request):
        return redirect(reverse_lazy('good_list'))


class Login(LoginView):
    template_name = 'login.html'
    authentication_form = LoginForm
    next_page = reverse_lazy('home_page')
    extra_context = {'title': 'Login', 'button': 'Sign in'}


class Logout(LogoutView):
    next_page = reverse_lazy('home_page')
