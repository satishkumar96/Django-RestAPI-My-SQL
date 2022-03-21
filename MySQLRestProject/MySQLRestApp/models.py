from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    city = models.CharField(max_length=200)
    created = models.DateField(auto_now=True)