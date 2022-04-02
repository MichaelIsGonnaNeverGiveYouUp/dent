from django.contrib import admin

from .models import Person, Customer

admin.site.register(Person)
admin.site.register(Customer)