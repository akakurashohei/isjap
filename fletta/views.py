from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from . models import *

class FlettaDetailView(DetailView):
    template_name = 'fletta/fletta.html'
    queryset = Fletta.objects.all()
    context_object_name = 'fletta'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['jp_jafnheiti_list'] = JpJafnheiti.objects.filter(uppflettiord_id = pk)
        return context
