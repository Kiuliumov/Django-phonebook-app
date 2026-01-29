from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    country_code = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=10)


    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)



class Account(AbstractUser):
    contacts = models.ForeignKey(to=Contact, on_delete=models.CASCADE, blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile_pictures", blank=True, null=True)
    has_agreed_cookies_notice = models.BooleanField(default=False)


