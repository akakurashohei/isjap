from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView
from functools import reduce
from operator import and_
from fletta.models import Fletta


class SearchResultView(ListView):
    template_name = 'leit/nidurstada.html'
    context_object_name = 'result_list'

    def get_queryset(self):
        if self.request.GET.get('q', ''):
            params = self.parse_search_params(self.request.GET['q'])
            query = reduce(
                lambda x,y : x & y,
                list(map(lambda z: Q(uppflettiord__iexact=z), params))
            )
            return Fletta.objects.filter(query)
        else:
            return None

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['query'] = self.request.GET.get('q', '')
        return ctx

    def parse_search_params(self, words: str):
        search_words = words.replace('　', ' ').split()
        return search_words
