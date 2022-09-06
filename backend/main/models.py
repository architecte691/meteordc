from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class City(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='media/cities', null=True)
    lat = models.FloatField(default=0.0)
    log = models.FloatField(default=0.0)
    surface = models.FloatField(default=0.0)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Moment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    datetime = models.DateTimeField()
    date_actu = models.DateField(null=True, blank=True)
    temperature = models.FloatField(default=0.0)
    cloud_description = models.TextField(default='')
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.temperature} {self.city}"