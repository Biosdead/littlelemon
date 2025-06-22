from django.db import models

# Create your models here.
class menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    inventory = models.IntegerField()
    
    def get_item(self):
        return f'{self.title} : {str(self.price)}'



class booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    bookingdate = models.DateTimeField()

class User(models.Model):
    url = models.URLField()
    username = models.CharField(max_length=255)
    email = models.EmailField()
    groups = models.CharField(max_length=255)