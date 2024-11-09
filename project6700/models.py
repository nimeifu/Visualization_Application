from django.db import models


#Create your models here.
class Karaoke(models.Model):
    partyID = models.IntegerField()
    NumberPeople = models.IntegerField()
    Hours = models.IntegerField()
    Session_Start_Time = models.IntegerField()
    locationID = models.CharField(max_length=100)
    Day_of_Week = models.CharField(max_length=100)


class Orders(models.Model):
    OrderID = models.CharField(max_length=100)
    Cost = models.DecimalField(max_digits=10, decimal_places=2)
    TimePlaced = models.DateTimeField()
    TimeDelivered = models.DateTimeField()


class Restaurant(models.Model):
    RestaurantID = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    Phone_number = models.CharField(max_length=255)
    Owner_name = models.CharField(max_length=255)
    Open_hours = models.CharField(max_length=255)

