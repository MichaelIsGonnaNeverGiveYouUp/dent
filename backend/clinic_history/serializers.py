from rest_framework import serializers
from .models import Customer, Person, Treatment, DentalPiece, Odontogram

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'first_name','last_name','document_type','document_id','gender','birth_date')


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'person','email','phone','work_title','company')


class TreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treatment
        fields = ('id', 'name','description')


class DentalPieceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DentalPiece
        fields = ('id', 'treatments','piece_number')


class OdontogramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Odontogram
        fields = ('id', 'customer','dental_piece')