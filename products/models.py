from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    barCode = models.CharField(max_length=100, unique=True, null=False, blank=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
