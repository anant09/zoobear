from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
	book_name= models.CharField(max_length=30)
	price=models.CharField(max_length=5)
	user=models.CharField(max_length=100)
	phone=models.CharField(max_length=10)
	
	def __str__(self):
		return self.book_name
	