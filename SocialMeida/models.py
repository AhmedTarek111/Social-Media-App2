from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_profile')
    profile_image = models.ImageField(upload_to='profile-user-image',default='user_default.png')
    bio= models.TextField(max_length=400,null=True,blank=True)
    location = models.CharField(max_length=200,null=True,blank=True)