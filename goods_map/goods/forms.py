from django import forms
from goods_map.goods.models import GoodsModel
from goods_map.stock import models


class GoodsForm(forms.ModelForm):
    name = forms.CharField(
        max_length=50, label='Name',
        widget=forms.TextInput(
            attrs={'id': 'id_name',
                   'class': 'form-control mb-3',
                   'placeholder': 'Name'}))

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

    class Meta:
        model = GoodsModel
        fields = ['name',
                  'cost_price',
                  'wholesale_price',
                  'retail_price',
                  'weight'
                  ]


class Storage(forms.ModelForm):
    store_hall = forms.ModelChoiceField(
        queryset=models.StoreHall.objects.all(), label='Store hall',
        required=False,
        widget=forms.Select(
            attrs={'id': 'id_store_hall',
                   'class': 'form-select mb-3'}))

    store_back = forms.ModelChoiceField(
        queryset=models.StoreBack.objects.all(), label='Store back',
        required=False,
        widget=forms.Select(
            attrs={'id': 'id_store_back',
                   'class': 'form-select mb-3'}))

    store_up = forms.ModelChoiceField(
        queryset=models.StoreUp.objects.all(), label='Store up',
        required=False,
        widget=forms.Select(
            attrs={'id': 'id_store_up',
                   'class': 'form-select mb-3'}))

    stock = forms.ModelMultipleChoiceField(
        queryset=models.StockModel.objects.all(), label='Stock',
        required=False,
        widget=forms.SelectMultiple(attrs={'id': 'id_labels',
                                           'class': 'form-select mb-3'}))

    class Meta:
        model = GoodsModel
        fields = [
            'store_hall',
            'store_back',
            'store_up',
            'stock'
            ]