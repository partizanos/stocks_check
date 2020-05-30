from django.db import models

# Create your models here.

class Stocks(models.Model):
    name = models.CharField(max_length=100)


class Price(models.Model):
    price = models.FloatField() 
    stocks = models.ForeignKey('Stocks', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.price