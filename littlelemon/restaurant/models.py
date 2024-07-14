import datetime
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateField(default=datetime.date.today)

class Menu(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(decimal_places=2,max_digits=10)
    Inventory = models.IntegerField()
    
    def __str__(self):
        return f'{self.title} : {self.price}'