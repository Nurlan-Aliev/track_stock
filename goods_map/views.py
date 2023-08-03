from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from goods_map.forms import LoginForm
from django_filters.views import FilterView
from goods_map.forms import FilterForm


class HomeView(LoginRequiredMixin, FilterView):
    template_name = 'index.html'
    filterset_class = FilterForm


class Login(LoginView):
    template_name = 'login.html'
    authentication_form = LoginForm
    next_page = reverse_lazy('home_page')
    extra_context = {'title': 'Login', 'button': 'Sign in'}


class Logout(LogoutView):
    next_page = reverse_lazy('home_page')
