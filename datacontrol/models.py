from django.db import models


# Create your models here.
class SalesPlan(models.Model):
    store_name = models.CharField(max_length=10)
    product1 = models.CharField(max_length=30, verbose_name='Симки')
    product2 = models.CharField(max_length=30, verbose_name='ГСМ')
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.store_name
