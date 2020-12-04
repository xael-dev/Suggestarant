from django.db import models


class Name(models.Model):
    restaurant_name = models.CharField(max_length=30)
    open_date = models.DateTimeField('date opened')

    def __str__(self):
        return self.restaurant_name


class Address(models.Model):
    restaurant_handle = models.ForeignKey(Name, on_delete=models.CASCADE)
    restaurant_address = models.CharField(max_length=100)

    def __str__(self):
        return self.restaurant_address


class Ratings(models.Model):
    restaurant_handle = models.ForeignKey(Name, on_delete=models.CASCADE)
    restaurant_ratings = models.IntegerField(
        default=0)  # Change to accept floats later on!

    def __str__(self):
        return self.restaurant_ratings
