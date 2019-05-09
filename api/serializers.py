# api/serializers.py
import googlemaps
from django.core.mail import EmailMessage
from rest_framework import serializers

from .models import Customer, Locality, Transport, Email, Scrapyard, Data, Request, Region


class CustomerSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    def create(self, validated_data):
        print(validated_data)
        obj, created = Customer.objects.update_or_create(phone=validated_data.get('phone', None),
                                                         defaults={'discount': validated_data.get('discount', None)})
        return obj

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Customer
        fields = ('id', 'phone', 'discount')


class LocalitySerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    def create(self, validated_data):
        print('Start')
        print(validated_data)
        name = validated_data.get('name', None)
        region = validated_data.get('region', None)
        locality = Locality.objects.create(**validated_data)

        origins = [name + ", " + region.name + ", Россия"]
        destinations = ["9 Мая ул., 210, Белогорск, Амурская обл., Россия, 676856",
                        "Красноармейская ул., 73, Сковородино, Амурская обл., Россия, 676011",
                        "пер. Станционный, Амурская обл., Россия, 676150",
                        "Промывочная ул., 15б, Хабаровск, Хабаровский край, Россия, 680032",
                        "Шоссейная ул., 128, Находка, Приморский край, Россия, 692906"]

        gmaps = googlemaps.Client(key='111')
        matrix = gmaps.distance_matrix(origins, destinations,
                                       mode="driving")

        try:
            print(matrix)
            elements = matrix['rows'][0]['elements']
            if (elements[0]['status'] == "ZERO_RESULTS"):
                raise Exception('Bad Address')
            locality.distanceBelogorsk = elements[0]['distance']['value']
            locality.distanceSkovorodino = elements[1]['distance']['value']
            locality.distanceTygda = elements[2]['distance']['value']
            locality.distanceKhabarovsk = elements[3]['distance']['value']
            locality.distanceNahotka = elements[4]['distance']['value']
            locality.region = region

            if (min(locality.distanceBelogorsk, locality.distanceSkovorodino, locality.distanceTygda,
                locality.distanceKhabarovsk) > 2500000):
                raise Exception('Bad Address')

            print(origins)
            print('End')
            locality.save()
            return locality
            
        except Exception:
            print('Error')
            locality.delete()
            return locality

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Locality
        fields = ('id', 'name', 'distanceBelogorsk', 'distanceSkovorodino', 'distanceTygda', 'distanceKhabarovsk',
                  'distanceNahotka', 'region')


class ScrapyardSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Scrapyard
        fields = ('name', 'price', 'coef', 'uid', 'transports')


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


class RegionSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    emails = EmailSerializer(many=True, read_only=True)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Region
        fields = ('id', 'name', 'emails', 'uid')


class RequestSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    def create(self, validated_data):
        request = Request.objects.create(**validated_data)
        emails = list(Email.objects.all().values_list("email", flat=True))
        email = EmailMessage('Заказ номер ' + request.id.__str__() + ' Телефон ' + request.phone,
                             'Заказ: ' + request.__str__(), to=emails)
        email.send()
        return request

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Request
        fields = (
            'id', 'phone', 'discount', 'region', 'locality', 'address', 'scrapyard', 'distantce', 'transport', 'cost',
            'tonn', 'price', 'data', 'comment', 'loader', 'cutter', 'calculatedInPlace', 'createdDate')


class DataSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    localitys = LocalitySerializer(many=True, read_only=True)
    transports = TransportSerializer(many=True, read_only=True)
    scrapyards = ScrapyardSerializer(many=True, read_only=True)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Data
        fields = ('id', 'loader', 'cutter', 'calculatedInPlace', 'transports', 'scrapyards', 'localitys', 'excessFare')
