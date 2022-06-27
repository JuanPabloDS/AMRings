from django.views.generic import TemplateView, DetailView
from django.shortcuts import redirect, render
from django.contrib import messages

from .forms import AnelModelForm

from .models import Anel

# Class based View
class IndexView(TemplateView):
    template_name: str = 'index.html'


    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['aneis'] = Anel.objects.all()
        return context


class AneisDetailView(DetailView):
    template_name: str = 'aneis.html'

    queryset = Anel.objects.all()


    def get_object(self):
        obj = super().get_object()
        return obj
