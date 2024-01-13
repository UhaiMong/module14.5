from django.db import models

# Create your models here.


class CollectionModel(models.Model):
    _id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    balance = models.BigIntegerField()
    agree = models.BooleanField()
    date = models.DateField()
    dateAndTime = models.DateTimeField()
    age = models.DecimalField(max_digits=5, decimal_places=2)
    duration = models.DurationField()
    email = models.EmailField()
    genericIP = models.GenericIPAddressField()

    def __str__(self):
        return f"Name: {self.name}"
