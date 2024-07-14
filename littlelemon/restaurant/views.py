from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from .serializers import UserSerializer, MenuSerializer, BookingSerializer
from rest_framework import generics
from rest_framework import viewsets
from .models import Menu, Booking
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()


def index(request):
    return render(request, 'index.html')


class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]