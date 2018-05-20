# from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics

# from api.form import SubscribeForm, AddressForm
from .models import Data, Locality, Scrapyard, Transport, Customer, Request
from .serializers import DataSerializer, CustomerSerializer, LocalitySerializer, ScrapyardSerializer, \
    TransportSerializer, RequestSerializer
from .forms import RequestForm


# import json
# from django.http import JsonResponse
# from django.views.generic import TemplateView
# from django.urls import reverse_lazy


class LocalityListView(generics.ListAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Locality.objects.all()
    serializer_class = LocalitySerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        queryset = Locality.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name=name)
        return queryset


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
        if phone is not None:
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

#
def post_list(request):
    objects = Data.objects.all()
    queryset = objects.get(pk=1)
    # make sure to catch 404's below

    # posts = Data.objects.all()

    return render(request, 'post_list.html', {'datas': queryset.scrapyards.all()})


def requestnew(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        # if form.is_valid():
        #     r = form.save()
        #     r.save()
    else:
        form = RequestForm()

    return render(request, 'request_new_edit.html', {'form': form})