from django import forms
from goods_map.goods.models import GoodsModel
from goods_map.stock.models import StockModel


class GoodsForm(forms.ModelForm):
    name = forms.CharField(
        max_length=50, label='Name',
        widget=forms.TextInput(
            attrs={'id': 'id_name',
                   'class': 'form-control mb-3',
                   'placeholder': 'Name'}))
    images = forms.ImageField(localize=2, required=False)
    cost_price = forms.IntegerField(
        label='Cost price',
        required=False,
        widget=forms.TextInput(
            attrs={'id': 'id_cost_price',
                   'class': 'form-control mb-3',
                   'placeholder': 'Write cost price'}))
    wholesale_price = forms.IntegerField(
        label='Wholesale price',
        required=False,
        widget=forms.TextInput(
            attrs={'id': 'id_wholesale_price',
                   'class': 'form-control mb-3',
                   'placeholder': 'Write Wholesale price'}))
    retail_price = forms.IntegerField(
        label='Retail price',
        required=False,
        widget=forms.TextInput(
            attrs={'id': 'id_retail_price',
                   'class': 'form-control mb-3',
                   'placeholder': 'Write Retail price'}))
    weight = forms.FloatField(
        label='Weight',
        required=False,
        widget=forms.TextInput(
            attrs={'id': 'id_retail_price',
                   'class': 'form-control mb-3',
                   'placeholder': 'Write weight of bag'}))

    stock = forms.ModelMultipleChoiceField(
        queryset=StockModel.objects.all(), label='Stock',
        required=False,
        widget=forms.SelectMultiple(attrs={'id': 'id_labels',
                                           'class': 'form-select mb-3'}))

    class Meta:
        model = GoodsModel
        fields = ['name', 'images', 'cost_price', 'wholesale_price', 'retail_price', 'weight', 'stock']
