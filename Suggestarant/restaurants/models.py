from django.db import models


class Name(models.Model):
    restaurant_name = models.CharField(max_length=30)
    open_date = models.DateTimeField('date opened')
    restaurant_address = models.CharField(max_length=100)
    restaurant_rating = models.IntegerField(default = 0)

    def __str__(self):
        return self.restaurant_name
