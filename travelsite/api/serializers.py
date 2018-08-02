from rest_framework import serializers
from api.models import (
    Airline,
    City,
    Hotel,
    Flight,
    FlightInstance
)

class AirlineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Airline
        fields = ('name',)


class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ('name', 'state', 'country')


class FlightSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Flight
        fields = (
            'flight_number',
            'airline',
            'source',
            'destination',
            'departure_time',
            'arrival_time',
            'miles',
            'international'
        )


class HotelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hotel
        fields = ('name', 'cities', 'number_of_rooms')
