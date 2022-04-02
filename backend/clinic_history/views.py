from django.shortcuts import render
from itsdangerous import Serializer
from rest_framework import viewsets
from .serializers import CustomerSerializer, PersonSerializer, TreatmentSerializer, OdontogramSerializer, DentalPieceSerializer
from .models import Customer, Person, Treatment, Odontogram, DentalPiece


class CustomerView(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class PersonView(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class TreatmentView(viewsets.ModelViewSet):
    serializer_class = TreatmentSerializer
    queryset = Treatment.objects.all()


class OdontogramView(viewsets.ModelViewSet):
    serializer_class = OdontogramSerializer
    queryset = Odontogram.objects.all()


class DentalPieceView(viewsets.ModelViewSet):
    serializer_class = DentalPieceSerializer
    queryset = DentalPiece.objects.all()