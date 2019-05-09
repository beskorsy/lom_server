# from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.shortcuts import render
from rest_framework import generics

# from api.form import SubscribeForm, AddressForm
from .models import Data, Locality, Scrapyard, Transport, Customer, Request, Email, Region
from .serializers import DataSerializer, CustomerSerializer, LocalitySerializer, ScrapyardSerializer, \
    TransportSerializer, RequestSerializer, RegionSerializer
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


class RegionListView(generics.ListAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


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


def requestnew(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            # req = Request()
            # req.phone = form.cleaned_data['phone']
            # req.loader = False
            # req.cutter = False
            # req.calculatedInPlace = False
            # req.discount = 0
            # req.locality = form.cleaned_data['locality']
            # req.address = form.cleaned_data['address']
            # req.scrapyard = form.cleaned_data['scrapyard']
            # req.distantce = 0
            # req.transport = form.cleaned_data['transport']
            # req.cost = 0
            # req.tonn = form.cleaned_data['tonn']
            # req.data = form.cleaned_data['data']
            # req.comment = form.cleaned_data['comment']
            # req.createdDate = 0
            # req.price = 0
            # req.save()
            #
            # emails = list(Email.objects.all().values_list("email", flat=True))
            # email = EmailMessage('Заказ номер ' + req.id.__str__() + ' Телефон ' + req.phone,
            #                  'Заказ: ' + req.__str__() + '\n Заказ сделан через сайт.', to=emails)
            # email.send()
            form = RequestForm()
    else:
        form = RequestForm()

    return render(request, 'request_new_edit.html', {'form': form})


def rule(request):

    return render(request, 'role.html')