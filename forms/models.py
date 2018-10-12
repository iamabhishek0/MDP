from django.db import models
from django.utils.timezone import now
import datetime

class FormSubmit(models.Model):
	#bookingID = models.CharField(max_length = 15, primary_key = True)
	name=models.CharField(max_length=30)
	email=models.CharField(max_length=30)
	street=models.TextField(max_length=300)
	city=models.CharField(max_length=30)
	number=models.CharField(max_length=30)
	pincode=models.CharField(max_length=30,blank=True,null=True)
	arrive=models.DateField(blank=True,null=True)
	depart=models.DateField(blank=True,null=True)
	reference_name=models.CharField(max_length=30,blank=True,null=True)
	reference_email=models.CharField(max_length=30,blank=True,null=True)
	room_type = models.CharField(max_length = 5,blank=True,null=True)

class Booking(models.Model):
	bookingID = models.CharField(max_length = 15,blank=True,null=True)
	roomID = models.CharField(max_length = 15,blank=True,null=True)
	arrive=models.DateField(blank=True,null=True)
	depart=models.DateTimeField(blank=True,null=True)

class Room(models.Model):
	roomID = models.CharField(max_length = 15,blank=True,null=True)
	room_type = models.CharField(max_length = 5,blank=True,null=True)
	status = models.CharField(max_length = 15,blank=True,null=True)

class ReferenceMail(models.Model):
	reference_name=models.CharField(max_length=30)
	reference_email=models.CharField(max_length=30)
