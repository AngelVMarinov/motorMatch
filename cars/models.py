from django.db import models

# Create your models here.
class Car(models.Model):
    brand = models.TextField()
    model = models.TextField()
    year = models.IntegerField()
    price = models.IntegerField()
    mileage = models.IntegerField()
    engine = models.TextField()
    transmission = models.TextField()
    fuel_type = models.TextField()
    color = models.TextField()
    location = models.TextField()
    description = models.TextField()
    image = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

