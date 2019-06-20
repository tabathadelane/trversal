from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from api.serializers import TripSerializer, DaySerializer, LocSerializer
from trversalapp.models import Trip, Day, Location
from trversalapp import gmaps



class TripViewSet(viewsets.ModelViewSet):
  
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

class DayViewSet(viewsets.ModelViewSet):
  
    queryset = Day.objects.all()
    serializer_class = DaySerializer

class ReCalcDay(generics.RetrieveAPIView):
  
    queryset = Day.objects.all()
    serializer_class = DaySerializer

    # def get_object(self):
    #     obj = super().get_object()
    #     gmaps.date_setter(obj)
    #     gmaps.time_gen(obj)
    #     return obj

    def dispatch(self, request, *args, **kwargs):

        day = Day.objects.get(pk=self.kwargs["pk"])
        gmaps.date_setter(day)
        gmaps.time_gen(day)
        return super().dispatch(request, *args, **kwargs)

class LocViewSet(viewsets.ModelViewSet):
  
    queryset = Location.objects.all()
    serializer_class = LocSerializer

class LocDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocSerializer

