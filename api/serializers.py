# api/serializers.py

from rest_framework import serializers

from .models import Customer, Locality, Transport, Email, Scrapyard, Data


class CustomerSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Customer
        fields = ('id', 'phone', 'discount')


class LocalitySerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Locality
        fields = ('id', 'name', 'distanceBelogorsk', 'distanceSkovorodino', 'distanceTygda')


class ScrapyardSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Scrapyard
        fields = ('id', 'name', 'price')


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


class DataSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    localitys = LocalitySerializer(many=True, read_only=True)
    transports = TransportSerializer(many=True, read_only=True)
    scrapyards = ScrapyardSerializer(many=True, read_only=True)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Data
        fields = ('id', 'loader', 'cutter', 'calculatedInPlace', 'transports', 'scrapyards', 'localitys')
