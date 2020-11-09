from django.db import models
from django.contrib.auth.models import User


class LastName(models.Model):
    lastname=models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.lastname