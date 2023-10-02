from django.views.generic import (CreateView,
                                  UpdateView)
from goods_map.count.forms import CountForm
from goods_map.count.models import CountGoods
from django.urls import reverse_lazy
from goods_map.goods.models import GoodsModel
from goods_map.mixin import AdminMixin


class AddGoodsView(AdminMixin, CreateView):
    template_name = 'edit.html'
    model = CountGoods
    form_class = CountForm
    success_url = reverse_lazy('good_list')
    extra_context = {'title': 'Add info', 'button': 'Add'}

    def form_valid(self, form):
        good = self.kwargs.get('pk')
        form.instance.good_id = GoodsModel.objects.get(id=good)
        form.save()
        return super().form_valid(form)


class UpdateCount(AdminMixin, UpdateView):
    template_name = 'edit.html'
    model = CountGoods
    form_class = CountForm
    success_url = reverse_lazy('good_list')
    extra_context = {'title': 'Update Count', 'button': 'Update'}
