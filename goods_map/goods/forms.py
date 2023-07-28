from django import forms
from goods_map.goods.models import GoodsModel


class GoodsForm(forms.ModelForm):
    name = forms.CharField(
        max_length=50, label='Name',
        widget=forms.TextInput(
            attrs={'id': 'id_name',
                   'class': 'form-control mb-3',
                   'placeholder': 'Name'}))
    cost_price = forms.IntegerField(
        label='Cost price',
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

    class Meta:
        model = GoodsModel
        fields = ['name', 'cost_price', 'wholesale_price', 'retail_price', 'weight']

