from django.conf.urls import url
from .views import FundListView, FundDetailView

urlpatterns = [

    url(r'^(?P<slug>[-\w]+)/$', FundDetailView.as_view(), name='fund_detail'),
    url(r'^$', FundListView.as_view(), name='fund_list'),

]

