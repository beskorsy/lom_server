# api/serializers.py
from django.core.mail import EmailMessage
from rest_framework import serializers
import googlemaps
from .models import Customer, Locality, Transport, Email, Scrapyard, Data, Request


class CustomerSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    def create(self, validated_data):
        obj, created = Customer.objects.update_or_create(phone = validated_data.get('phone', None),
                                                         defaults={'discount': validated_data.get('discount', None)})
        return obj

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Customer
        fields = ('id', 'phone', 'discount')


class LocalitySerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    def create(self, validated_data):
        name = validated_data['name']
        locality = Locality.objects.create(**validated_data)

        origins = [name + ", Амурская область, Россия"]
        destinations = ["Белогорск, Амурская область, Россия",
                        "Сковородино, Амурская область, Россия",
                        "Тыгда, Амурская область, Россия"]

        gmaps = googlemaps.Client(key='111')
        matrix = gmaps.distance_matrix(origins, destinations,
                                       mode="driving")

        try:
            elements = matrix['rows'][0]['elements']
            locality.distanceBelogorsk = elements[0]['distance']['value']
            locality.distanceSkovorodino = elements[1]['distance']['value']
            locality.distanceTygda = elements[2]['distance']['value']

            locality.save()
            return locality

        except Exception:
            locality.delete()


    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Locality
        fields = ('id', 'name', 'distanceBelogorsk', 'distanceSkovorodino', 'distanceTygda')


class ScrapyardSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Scrapyard
        fields = ('id', 'name', 'price', 'coef')


class TransportSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Transport
        fields = ('id', 'name', 'price', 'tonn')


class EmailSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Email
        fields = ('id', 'email')

class RequestSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""


    def create(self, validated_data):
        request = Request.objects.create(**validated_data)
        emails = list(Email.objects.all().values_list("email", flat=True))
        email = EmailMessage('Заказ номер '+ request.id.__str__() + ' Телефон ' + request.phone,
                             'Заказ: ' + request.__str__(), to=emails)
        email.send()
        return super(RequestSerializer, self).create(validated_data)


    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Request
        fields = ('id', 'phone', 'discount', 'locality', 'address', 'scrapyard', 'distantce', 'transport', 'cost', 'tonn',
                  'data', 'comment', 'loader', 'cutter', 'calculatedInPlace', 'createdDate')

class DataSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    localitys = LocalitySerializer(many=True, read_only=True)
    transports = TransportSerializer(many=True, read_only=True)
    scrapyards = ScrapyardSerializer(many=True, read_only=True)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Data
        fields = ('id', 'loader', 'cutter', 'calculatedInPlace', 'transports', 'scrapyards', 'localitys')
