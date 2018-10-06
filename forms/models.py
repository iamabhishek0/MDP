from django.db import models
from django.utils.timezone import now
import datetime

# Create your models here.
class FormSubmit(models.Model):


		name=models.CharField(max_length=30)
		email=models.CharField(max_length=30)
		street=models.TextField(max_length=300)
		city=models.CharField(max_length=30)
		number=models.CharField(max_length=30)
		pincode=models.CharField(max_length=30,blank=True,null=True)
		arrive=models.DateField(blank=True,null=True)
		depart=models.DateTimeField(blank=True,null=True)
	   






class ReferenceMail(models.Model):
	reference_name=models.CharField(max_length=30)
	reference_email=models.CharField(max_length=30)
		
		
				