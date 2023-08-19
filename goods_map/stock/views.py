from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView
from goods_map.stock.forms import StockForm, MarketForm
from goods_map.stock.models import StockModel, MarketModel
from django.urls import reverse_lazy


class StockHome(ListView):
    template_name = 'stock.html'
    model = StockModel


class CreateStock(LoginRequiredMixin, CreateView):
    template_name = 'edit.html'
    model = StockModel
    form_class = StockForm
    success_url = reverse_lazy('good_list')
    extra_context = {'title': 'Create stock place', 'button': 'Create'}


class CreateMarket(LoginRequiredMixin, CreateView):
    template_name = 'edit.html'
    model = MarketModel
    form_class = MarketForm
    success_url = reverse_lazy('good_list')
    extra_context = {'title': 'Create market place', 'button': 'Create'}
