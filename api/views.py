from django.http import JsonResponse
from rest_framework import generics

import json
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.urls import reverse_lazy

from api.form import SubscribeForm, AddressForm
from .models import Data, Locality, Scrapyard, Transport, Customer, Request
from .serializers import DataSerializer, CustomerSerializer, LocalitySerializer, ScrapyardSerializer, \
    TransportSerializer, RequestSerializer


class LocalityListView(generics.ListAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Locality.objects.all()
    serializer_class = LocalitySerializer


class LocalityListCreateView(generics.ListCreateAPIView):
    queryset = Locality.objects.all()
    serializer_class = LocalitySerializer


class RequestCreateView(generics.ListCreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class RequestListView(generics.ListAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class ScrapyardListView(generics.ListAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Scrapyard.objects.all()
    serializer_class = ScrapyardSerializer


class TransportListView(generics.ListAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer


class DataView(generics.RetrieveAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Data.objects.all()
    serializer_class = DataSerializer

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        # make sure to catch 404's below
        obj = queryset.get(pk=1)
        self.check_object_permissions(self.request, obj)
        return obj


class CustomerRetrieveView(generics.ListCreateAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerListView(generics.ListAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    serializer_class = CustomerSerializer
    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        queryset = Customer.objects.all()
        phone = self.request.query_params.get('phone', None)
        if phone  is not None:
            queryset = queryset.filter(phone='+' + phone)
        return queryset


# class CreateLocalityView(generics.ListCreateAPIView):
#     """This class defines the create behavior of our rest api."""
#     queryset = Locality.objects.all()
#     serializer_class = LocalitySerializer
#
#     def perform_create(self, serializer):
#         """Save the post data when creating a new bucketlist."""
#         serializer.save()
#
#
# class DetailsLocalityView(generics.RetrieveUpdateDestroyAPIView):
#     """This class handles the http GET, PUT and DELETE requests."""
#
#     queryset = Locality.objects.all()
#     serializer_class = LocalitySerializer


class SubscribeView(TemplateView):
    template_name = 'index.html'
    success_url = reverse_lazy('form_data_valid')

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['subscribe_form'] = SubscribeForm()
        context['address_form'] = AddressForm()
        return self.render_to_response(context)

    def put(self, request, *args, **kwargs):
        request_data = json.loads(request.body)
        subscribe_form = SubscribeForm(data=request_data.get(SubscribeForm.scope_prefix, {}))
        address_form = AddressForm(data=request_data.get(AddressForm.scope_prefix, {}))
        response_data = {}

        if subscribe_form.is_valid() and address_form.is_valid():
            response_data.update({'success_url': self.success_url})
            return JsonResponse(response_data)

        # otherwise report form validation errors
        response_data.update({
            subscribe_form.form_name: subscribe_form.errors,
            address_form.form_name: address_form.errors,
        })
        return JsonResponse(response_data, status=422)