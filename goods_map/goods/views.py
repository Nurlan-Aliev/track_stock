import math
from django.shortcuts import render
from django.views.generic import (ListView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,
                                  TemplateView)
from django.views import View
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

    def form_valid(self, form):

        if not form.instance.wholesale_price:
            weight = form.instance.weight if form.instance.weight else 1
            form.instance.wholesale_price = math.ceil(
                (form.instance.cost_price * 0.27) + (weight * 6) + 2)
            print()
            print(form.instance.wholesale_price)
            print()
        if not form.instance.retail_price:
            form.instance.retail_price = form.instance.wholesale_price + 7

        form.save()
        return super().form_valid(form)


class UpdateGood(UpdateView):
    template_name = 'edit.html'
    model = GoodsModel
    form_class = GoodsForm
    success_url = reverse_lazy('good_list')


class DeleteGood(DeleteView):
    template_name = 'delete.html'
    model = GoodsModel
    success_url = reverse_lazy('good_list')


class GoodCard(View):
    template_name = 'good_card.html'

    def get(self, request, *args, **kwargs):
        goods_id = kwargs.get('pk')
        good = GoodsModel.objects.get(id=goods_id)
        return render(request, self.template_name,
                      {'good': good})


