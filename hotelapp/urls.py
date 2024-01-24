from django.urls import path
from hotelapp.views import index, room, contact, fa,booking


urlpatterns = [
    path('', index, name='index'),
    path('room/', room, name='room'),
    path('contact/', contact, name='contact'),
    path('fa/', fa, name='fa'),
    path('booking/', booking, name='booking'),
]
