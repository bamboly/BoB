from django.db import models

# Create your models here.
class Product(models.Model):
	title 		= models.CharField(max_length = 130)
	price 		= models.DecimalField(max_digits=10000, decimal_places = 2)
	description = models.TextField(blank=False , null =False)
	summary 	= models.TextField(blank=False ,null =False)
	features	= models.BooleanField()