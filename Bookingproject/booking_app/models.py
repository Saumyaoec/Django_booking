from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models import DateTimeField
from django.utils import timezone


#Create your models here.

class Address(models.Model):
    street = models.TextField()
    city = models.TextField()
    province = models.TextField()
    zip_code = models.TextField()

    def __str__(self):
      return self.street



STATUS_BOOKING = (
      ('initiated','Initiated'),
      ('pending','Pending'),
      ('confirm','Confirm'),
      ('cancel','Cancel'),
      ('completed','Completed')
      )


GENDER_CHOICES =(
         ('M', 'Male'),
         ('F', 'Female')
        )

class Booking(models.Model):

   user = models.ForeignKey(User, on_delete=models.CASCADE)
   gender = models.CharField(max_length=100,choices=GENDER_CHOICES,default = 'M')
   firstname = models.CharField(max_length=100)
   lastname = models.CharField(max_length=30)
   nationality = CountryField(blank=True)
   address = models.ForeignKey(Address,on_delete = models.CASCADE)
   email=models.EmailField(max_length = 50)
   mobile_Number=models.BigIntegerField()
   date_from = models.DateTimeField()
   date_until = models.DateTimeField()
   # creation_date = models.DateTimeField(auto_now_add = True)
   creation_date = models.DateTimeField(default=timezone.now,null=True)
   booking_status = models.CharField(max_length=100,choices=STATUS_BOOKING)
   #property_type = models.ForeignKey()
   cost = models.DecimalField(max_digits = 10,decimal_places =2,null = True)
   notes = models.TextField()









		