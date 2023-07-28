from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View


class HomeView(View):
    def get(self, request):
        return redirect(reverse_lazy('good_list'))

