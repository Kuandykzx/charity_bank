from django.conf.urls import url
from .views import CaseListView, CaseDetailView

urlpatterns = [

    url(r'^(?P<slug>[-\w]+)/$', CaseDetailView.as_view(), name='detail'),
    url(r'^$', CaseListView.as_view(), name='list'),

]

