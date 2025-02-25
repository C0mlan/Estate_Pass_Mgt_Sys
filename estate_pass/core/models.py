from django.db import models
import random
from django.contrib.auth.models import User
        
class Guest(models.Model):
    flat_no= models.ForeignKey(User, on_delete=models.CASCADE)
    name= models.CharField(max_length=100)
    purpose= models.TextField(max_length=100)
    code = models.CharField(max_length=10, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)



    