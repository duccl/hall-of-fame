from django.db import models


class Hall(models.Model):
    author = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100,default='')
    creation_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Video(models.Model):
    hall = models.ForeignKey(Hall,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    youtube_id = models.CharField(max_length=255)

    def __str__(self):
        return self.title