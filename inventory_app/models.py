from django.db import models

from django.contrib.auth.models import AbstractUser
class Inventory(models.Model):
    item_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    last_updated = models.DateTimeField(auto_now=True)

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('staff', 'Staff'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='staff')
