from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import DetailView, ListView, UpdateView, RedirectView
from django.utils import timezone
from .models import Fund
# Create your views here.


class FundDetailView(DetailView):
    model = Fund
    slug_field = 'id'

    def get_context_data(self, **kwargs):
        context = super(FundDetailView, self).get_context_data(**kwargs)
        return context


class FundListView(ListView):

    model = Fund
    context_object_name = 'fund_list'
    slug_field = 'id'

    def get_context_data(self, **kwargs):
        context = super(FundListView, self).get_context_data(**kwargs)
        return context
