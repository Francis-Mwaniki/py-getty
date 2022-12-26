from django.db import models
from django.contrib.auth.models import AbstractUser
import os

class CustomUser(AbstractUser):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join("Users", self.username, instance)
        return None

    STATUS =(
        ('regular', 'regular'),
        ('subscriber', 'subscriber'),
        ('moderator', 'moderator'),
         )
    email = models.EmailField(unique=True)
    status= models.CharField(max_length=100, choices=STATUS, default='regular')
    description= models.TextField('Description',max_length=600,default='',blank=True)
    image = models.ImageField(default='default/dennis.jpg', upload_to=image_upload_to)
    
    def __str__(self):
        return self.username
    

