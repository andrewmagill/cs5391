from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register(r'cities', views.CityViewSet)
router.register(r'airlines', views.AirlineViewSet)
router.register(r'flights', views.FlightViewSet)
router.register(r'hotels', views.HotelViewSet)

urlpatterns= [
    url(r'^', include(router.urls))
]
