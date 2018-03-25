from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import LocalityListView, ScrapyardListView, TransportListView, CustomerRetrieveView, DataView, \
    LocalityListCreateView, RequestCreateView, CustomerListView

urlpatterns = {
    url(r'^scrapyard/', ScrapyardListView.as_view(), name="Scrapyard list"),
    url(r'^api/data', DataView.as_view(), name="Data list"),
    url(r'^locality/', LocalityListView.as_view(), name="Locality list"),
    url(r'^localityadd/', LocalityListCreateView.as_view(), name="Locality add list"),
    url(r'^requestadd/', RequestCreateView.as_view(), name="Request list"),
    url(r'^transport/', TransportListView.as_view(), name="Transport list"),
    url(r'^customer/$', CustomerListView.as_view(), name="Customer list"),
    url(r'^customerupdate/', CustomerRetrieveView.as_view(), name="Customer update"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
