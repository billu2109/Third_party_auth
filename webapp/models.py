from django.contrib.auth.models import User
from django.db import models



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    email = models.EmailField()
    mobile_num = models.CharField(max_length=12)
    DOB = models.DateField(null=True,blank=True)
