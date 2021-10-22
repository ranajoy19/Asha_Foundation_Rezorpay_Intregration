from django.db import models


# Create your models here.
class Donation(models.Model):
    name = models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    amount=models.CharField(max_length=200)
    payment_id=models.CharField(max_length=200)
    paid=models.BooleanField(default=False)

    def __str__(self):
        return self.name