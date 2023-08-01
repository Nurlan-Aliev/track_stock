from django import forms
from goods_map.count.models import CountGoods


class CountForm(forms.ModelForm):
    count = forms.IntegerField(
        label='Count of goods',
        widget=forms.TextInput(
            attrs={'id': 'id_count',
                   'class': 'form-control mb-3',
                   'placeholder': 'Write count'}))

    cost_price = forms.IntegerField(
        label='Cost price',
        widget=forms.TextInput(
            attrs={'id': 'id_cost_price',
                   'class': 'form-control mb-3',
                   'placeholder': 'Write cost price'}))

    class Meta:
        model = CountGoods
        fields = ['count', 'cost_price']
