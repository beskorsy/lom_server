from rest_framework import generics

from .models import Data, Locality, Scrapyard, Transport, Customer
from .serializers import DataSerializer, CustomerSerializer, LocalitySerializer, ScrapyardSerializer, \
    TransportSerializer


class LocalityListView(generics.ListAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Locality.objects.all()
    serializer_class = LocalitySerializer


class LocalityListCreateView(generics.ListCreateAPIView):
    queryset = Locality.objects.all()
    serializer_class = LocalitySerializer


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


class CustomerRetrieveView(generics.ListAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    serializer_class = CustomerSerializer
    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """

        # http://localhost:8000/customer/?format=json&phone=79039225020
        # return Customer.objects.filter(phone='+'+ self.request.query_params.get('phone'))

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
