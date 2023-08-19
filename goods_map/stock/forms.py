from django import forms
from goods_map.stock.models import StockModel, MarketModel


class StockForm(forms.ModelForm):
    name = forms.CharField(
        label='Stock',
        widget=forms.TextInput(
            attrs={'id': 'id_stock',
                   'class': 'form-control mb-3',
                   'placeholder': 'Stock name'}))

    class Meta:
        model = StockModel
        fields = ['name']


class MarketForm(forms.ModelForm):
    name = forms.CharField(
        label='Market',
        widget=forms.TextInput(
            attrs={'id': 'id_market',
                   'class': 'form-control mb-3',
                   'placeholder': 'Stock name'}))

    class Meta:
        model = MarketModel
        fields = ['name']
