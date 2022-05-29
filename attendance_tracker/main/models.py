from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Post(models.Model):
    name=models.CharField(max_length=255)
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_pic=models.ImageField(null=True, blank=True, upload_to='images/profile')

    def __str__(self):
        return str(self.user)

class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    