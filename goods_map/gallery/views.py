from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from goods_map.gallery.models import GoodsModel, ImageModel
from goods_map.gallery.forms import ImageForm
from django.urls import reverse_lazy


class AddImageView(LoginRequiredMixin, CreateView):
    template_name = 'edit.html'
    model = ImageModel
    form_class = ImageForm
    success_url = reverse_lazy('good_list')
    extra_context = {'title': 'Add foto', 'button': 'ADD'}

    def form_valid(self, form):
        product_id = self.kwargs.get('pk')
        form.instance.product_id = GoodsModel.objects.get(id=product_id)
        form.save()
        return super().form_valid(form)
