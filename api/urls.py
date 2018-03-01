from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import LocalityListView, ScrapyardListView, TransportListView, CustomerRetrieveView, DataView

urlpatterns = {
    url(r'^scrapyard/', ScrapyardListView.as_view(), name="Scrapyard list"),
    url(r'^api/data', DataView.as_view(), name="Data list"),
    url(r'^locality/', LocalityListView.as_view(), name="Locality list"),
    url(r'^transport/', TransportListView.as_view(), name="Transport list"),
    # url(r'^setting/(?P<pk>[0-9]+)/$', SettingRetrieveView.as_view(), name="Setting list"),
    url(r'^customer/$', CustomerRetrieveView.as_view(), name="Customer list"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
