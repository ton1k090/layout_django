from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from home_app.models import Trainer


class HomeView(ListView):
    model = Trainer
    template_name = 'home_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trainers_list'] = Trainer.objects.all()
        return context
