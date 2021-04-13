from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings

class Brand(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Seller(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(
        max_length=128,
        validators=[MinLengthValidator(2, "Title must be greater than 2 characters")]
    )
    seller = models.ManyToManyField('Seller', through='Listing', related_name='seller')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    manufacture_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Listing(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=True)



