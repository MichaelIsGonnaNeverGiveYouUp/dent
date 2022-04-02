from django.db import models


document_types = (
    ('DNI', 'Documento Nacional de Identidad'),
    ('PAS', 'Pasaporte'),
    ('CE', 'Carnet de Extranjeria'),
)

genders = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)


class Person(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)

    document_id = models.CharField(max_length=30)
    birth_date = models.DateField()
    document_type = models.CharField(
        choices=document_types, max_length=50, default="")
    gender = models.CharField(choices=genders, max_length=50, default="")

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class Customer(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    work_title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.email}"


class Treatment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"


class DentalPiece(models.Model):
    treatments = models.ManyToManyField(Treatment)
    piece_number = models.IntegerField()

    def __str__(self):
        return f"{self.piece_number}"
    

class Odontogram(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    dental_piece = models.ManyToManyField(DentalPiece)

    def __str__(self):
        return f"{self.dental_piece}"

