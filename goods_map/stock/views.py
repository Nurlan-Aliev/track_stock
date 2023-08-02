from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from goods_map.stock.forms import StockForm
from goods_map.stock.models import StockModel
from django.urls import reverse_lazy


class CreateStock(LoginRequiredMixin, CreateView):
    template_name = 'edit.html'
    model = StockModel
    form_class = StockForm
    success_url = reverse_lazy('good_list')
    extra_context = {'title': 'Create Stock', 'button': 'Create'}
