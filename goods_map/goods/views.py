import math
from django.views.generic import (ListView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,
                                  DetailView)
from goods_map.goods.models import GoodsModel
from goods_map.goods.forms import GoodsForm
from django.urls import reverse_lazy


class GoodsList(ListView):
    template_name = 'goods_list.html'
    model = GoodsModel


class CreateGood(CreateView):
    template_name = 'edit.html'
    model = GoodsModel
    form_class = GoodsForm
    success_url = reverse_lazy('good_list')
    extra_context = {'title': 'Create Good', 'button': 'Create'}

    def form_valid(self, form):

        if not form.instance.wholesale_price:
            weight = form.instance.weight if form.instance.weight else 1
            form.instance.wholesale_price = math.ceil(
                (form.instance.cost_price * 0.27) + (weight * 6) + 2)
        if not form.instance.retail_price:
            form.instance.retail_price = form.instance.wholesale_price + 7

        form.save()
        return super().form_valid(form)


class UpdateGood(UpdateView):
    template_name = 'edit.html'
    model = GoodsModel
    form_class = GoodsForm
    success_url = reverse_lazy('good_list')
    extra_context = {'title': 'Update Good', 'button': 'Update'}


class DeleteGood(DeleteView):
    template_name = 'delete.html'
    model = GoodsModel
    success_url = reverse_lazy('good_list')


class GoodCard(DetailView):
    template_name = 'good_card.html'
    model = GoodsModel
