from django.db import models

class Product(models.Model):
    title       = models.CharField(max_length=120) 
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(max_digits=100000, decimal_places=2)
    summary     = models.TextField(default = "this is summary cool!!!!")