from django.db import models


class Name(models.Model):
    restaurant_name = models.CharField(max_length=30)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.restaurant_name

class Location(models.Model):
    restaurant = models.ForeignKey(Name, on_delete=models.CASCADE)
    public_address = models.CharField(max_length=100)

    def __str__(self):
        return self.public_address
    