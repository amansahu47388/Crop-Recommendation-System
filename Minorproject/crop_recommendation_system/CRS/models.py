from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomManager
# Create your models here.


class CustomUser(AbstractUser):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    username = None
    email = models.EmailField("Email",unique=True, blank=False)
    phone = models.CharField(max_length=10, blank=False)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, blank=False)
    image = models.ImageField(upload_to='images',null=True, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= []

    objects = CustomManager()

    def __str__(self):
        return self.email

