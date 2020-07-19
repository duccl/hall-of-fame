from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='profilePic',blank=True,upload_to='accounts_pics')
    about = models.CharField(max_length=250,blank=True)

    def __str__(self):
        return self.user.username
