from django import forms
from goods_map.stock.models import StockModel


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
