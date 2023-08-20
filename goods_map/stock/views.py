from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from goods_map.stock.forms import StockForm, MarketForm
from goods_map.stock.models import StockModel, MarketModel
from django.urls import reverse_lazy


class StockHome(LoginRequiredMixin, ListView):
    template_name = 'stock.html'
    model = StockModel

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['market'] = MarketModel
        return context


class CreateStock(LoginRequiredMixin, CreateView):
    template_name = 'edit.html'
    model = StockModel
    form_class = StockForm
    success_url = reverse_lazy('stock_home')
    extra_context = {'title': 'Create stock place', 'button': 'Create'}


class CreateMarket(LoginRequiredMixin, CreateView):
    template_name = 'edit.html'
    model = MarketModel
    form_class = MarketForm
    success_url = reverse_lazy('stock_home')
    extra_context = {'title': 'Create market place', 'button': 'Create'}
