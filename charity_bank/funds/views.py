from django.views.generic import DetailView, ListView
from .models import Fund


class FundDetailView(DetailView):
    model = Fund
    slug_field = 'id'


class FundListView(ListView):

    model = Fund
    context_object_name = 'fund_list'
    slug_field = 'id'

