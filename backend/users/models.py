from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    lat = models.FloatField(default=0.0)
    log = models.FloatField(default=0.0)
    surface = models.FloatField(default=0.0)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"subscription {self.name}"
