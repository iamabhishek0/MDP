from django.db import models
from django.utils.timezone import now
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings

class FormSubmit(models.Model):
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
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	bookingID = models.CharField(max_length = 15,blank=True,null=True)
	roomID = models.CharField(max_length = 15,blank=True,null=True)
	name = models.CharField(max_length=30,blank=True,null=True)
	arrive = models.DateField(blank=True,null=True)
	depart = models.DateField(blank=True,null=True)

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	reference_verified=models.BooleanField(default=False)
	director_verified=models.BooleanField(default=False)
	verified=models.BooleanField(default=False)
	booking_mail_sent=models.BooleanField(default=False)
	street=models.TextField(max_length=300,blank=True,null=True)
	city=models.CharField(max_length=30,blank=True,null=True)
	number=models.CharField(max_length=30,blank=True,null=True)
	pincode=models.CharField(max_length=30,blank=True,null=True)
	arrive=models.DateField(blank=True,null=True)
	depart=models.DateField(blank=True,null=True)
	reference_name=models.CharField(max_length=30,blank=True,null=True)
	reference_email=models.CharField(max_length=30,blank=True,null=True)
	is_member=models.BooleanField(default=False)
	applied_for_member=models.BooleanField(default=False)
	#room_type = models.CharField(max_length = 5,blank=True,null=True)

	#other fields here

	def __str__(self):
		  return "%s's profile" % self.user

def create_user_profile(sender, instance, created, **kwargs):
	if created:
	   profile, created = UserProfile.objects.get_or_create(user=instance)
	   profile, created = Booking.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)

class Room(models.Model):
	roomID = models.CharField(max_length = 15,blank=True,null=True)
	room_type = models.CharField(max_length = 5,blank=True,null=True)
	status = models.CharField(max_length = 15,blank=True,null=True)
