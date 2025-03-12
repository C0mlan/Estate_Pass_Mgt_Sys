from django.db import models
from django.contrib.auth.models import User


        
class Guest(models.Model):
    flat_no= models.ForeignKey(User, on_delete=models.CASCADE)
    name= models.CharField(max_length=100)
    purpose= models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
class Passer(models.Model):
    user = models.OneToOneField(Guest, on_delete=models.CASCADE)
    code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user.name}--{self.code}"



