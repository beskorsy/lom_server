# api/serializers.py

from rest_framework import serializers

from .models import Customer, Locality, Transport, Email, Scrapyard, Setting


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


class SettingSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Setting
        fields = ('id', 'loader', 'cutter','calculatedInPlace')
