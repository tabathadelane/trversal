from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from api.serializers import TripSerializer, LocSerializer
from trversalapp.models import Trip, Location
from trversalapp import gmaps

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class IsCreatorOrReadOnlyTrip(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.creator == request.user

class IsCreatorOrReadOnlyDay(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.trip_name.creator == request.user

class TripViewSet(viewsets.ModelViewSet):
    permission_classes = (IsCreatorOrReadOnlyTrip,)
  
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

# class DayViewSet(viewsets.ModelViewSet):
#     permission_classes = (IsCreatorOrReadOnlyDay,)
#     queryset = Day.objects.all()
#     serializer_class = DaySerializer

class ReCalcTrip(generics.RetrieveAPIView):
  
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    def dispatch(self, request, *args, **kwargs):

        trip = Trip.objects.get(pk=self.kwargs["pk"])
        # gmaps.date_setter(day)
        gmaps.time_gen(trip)
        return super().dispatch(request, *args, **kwargs)

class LocViewSet(viewsets.ModelViewSet):
  
    queryset = Location.objects.all()
    serializer_class = LocSerializer

class LocDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocSerializer

