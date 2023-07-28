from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class StockView(TemplateView):
    template_name = 'stock.good.html'
