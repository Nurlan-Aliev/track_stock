from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from goods_map.stock import models


class StockHome(LoginRequiredMixin, ListView):
    template_name = 'stock.html'
    model = models.StockModel

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['store_hall'] = models.StoreHall.objects.all()
        context['store_back'] = models.StoreBack.objects.all()
        context['store_up'] = models.StoreUp.objects.all()
        return context
