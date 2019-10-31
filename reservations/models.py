from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    gender = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    nationality = models.IntegerField()
    grade = models.IntegerField()

class Reservation(models.Model):
    checkin = models.DateTimeField()
    checkout = models.DateTimeField()
    adults = models.IntegerField()
    kids = models.IntegerField()
    customers = models.ManyToManyField(Customer, related_name='reservations', blank=True)
    josik = models.BooleanField()
    swimming_pool = models.BooleanField()
    lounge = models.BooleanField()
    creditCatd = models.TextField()
    peopleNum = models.IntegerField()

class Room(models.Model):
    bed = models.CharField(max_length=50)
    capacity = models.IntegerField()
    price = models.IntegerField()
    view = models.IntegerField()
    floor = models.IntegerField()
    roomnumber = models.IntegerField()
    smokable = models.BooleanField
    ammenities = models.TextField()
