from django.db import models

# Create your models here.
class FormSubmit(models.Model):

	name=models.CharField(max_length=30)
	email=models.CharField(max_length=30)
	street=models.TextField(max_length=300)
	city=models.CharField(max_length=30)
	number=models.CharField(max_length=30)
	