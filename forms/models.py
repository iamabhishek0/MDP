from django.db import models
from django.utils.timezone import now
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save

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
	name = models.CharField(max_length=30,blank=True,null=True)
	arrive=models.DateField(blank=True,null=True)
	depart=models.DateField(blank=True,null=True)

class Room(models.Model):
	roomID = models.CharField(max_length = 15,blank=True,null=True)
	room_type = models.CharField(max_length = 5,blank=True,null=True)
	status = models.CharField(max_length = 15,blank=True,null=True)

class ReferenceMail(models.Model):
	reference_name=models.CharField(max_length=30)
	reference_email=models.CharField(max_length=30)

class UserProfile(models.Model):
	user = models.OneToOneField(User,related_name='userprofile', on_delete=models.CASCADE)
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
	#room_type = models.CharField(max_length = 5,blank=True,null=True)

	#other fields here

	def __str__(self):
		  return "%s's profile" % self.user

def create_user_profile(sender, instance, created, **kwargs):
	if created:
	   profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)
