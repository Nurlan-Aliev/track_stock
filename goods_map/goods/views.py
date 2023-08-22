import math
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (CreateView,
                                  UpdateView,
                                  DeleteView,
                                  DetailView)

from goods_map.forms import FilterForm
from goods_map.goods.models import GoodsModel
from goods_map.goods.forms import GoodsForm, Storage
from django.urls import reverse_lazy
from django_filters.views import FilterView

from goods_map.mixin import AdminMixin


class GoodsList(LoginRequiredMixin, FilterView):
    template_name = 'goods_list.html'
    model = GoodsModel
    filterset_class = FilterForm


class CreateGood(AdminMixin, CreateView):
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


class UpdateGood(AdminMixin, UpdateView):
    template_name = 'edit.html'
    model = GoodsModel
    form_class = GoodsForm
    success_url = reverse_lazy('good_list')
    extra_context = {'title': 'Update Good', 'button': 'Update'}


class DeleteGood(AdminMixin, DeleteView):
    template_name = 'delete.html'
    model = GoodsModel
    success_url = reverse_lazy('good_list')


class GoodCard(LoginRequiredMixin, DetailView):
    template_name = 'good_card.html'
    model = GoodsModel


class UpdateStorage(LoginRequiredMixin, UpdateView):
    template_name = 'edit.html'
    model = GoodsModel
    form_class = Storage
    success_url = reverse_lazy('home_page')
    extra_context = {'title': 'Update Storage', 'button': 'Update'}


