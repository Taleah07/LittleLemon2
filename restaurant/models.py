from django.db import models

# Create your models here.
class booking(models.Model):
    Id = models.IntegerField(11, primary_key=True)
    Name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(6)
    bookingdate = models.DateTimeField()

class menu(models.Model):
    id = models.IntegerField(5,primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(5)

def __str__(self):
    return f'{self.title} : {str(self.price)}'
