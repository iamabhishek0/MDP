from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class BookingTable(models.Model):
	bookingID = models.CharField(max_length=15, blank=True, null=True)
	roomID = models.CharField(max_length=15, blank=True, null=True)
	name = models.CharField(max_length=30, blank=True, null=True)
	arrive = models.DateField(blank=True, null=True)
	depart = models.DateField(blank=True, null=True)


class FormSubmit(models.Model):
	userbookings=models.ForeignKey(User,on_delete=models.CASCADE)
	bookingtable=models.OneToOneField(BookingTable,on_delete=models.CASCADE,blank=True, null=True)
	name = models.CharField(max_length=30)
	email = models.CharField(max_length=30)
	street = models.TextField(max_length=300)
	city = models.CharField(max_length=30)
	number = models.CharField(max_length=30)
	pincode = models.CharField(max_length=30, blank=True, null=True)
	arrive = models.DateField(blank=True, null=True)
	depart = models.DateField(blank=True, null=True)
	reference_name = models.CharField(max_length=30, blank=True, null=True)
	reference_email = models.CharField(max_length=30, blank=True, null=True)
	room_type = models.CharField(max_length=5, blank=True, null=True)
	reference_verified=models.BooleanField(default=False)
	director_verified=models.BooleanField(default=False)
	verified=models.BooleanField(default=False)
	booking_mail_sent=models.BooleanField(default=False)
	admin_verified=models.BooleanField(default=False)
	def room(self):
		return self.bookingtable.roomID
