# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets

from api.models import Airline, City, Flight, Hotel
from api.serializers import (
    AirlineSerializer,
    CitySerializer,
    FlightSerializer,
    HotelSerializer,
)

class AirlineViewSet(viewsets.ModelViewSet):
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
