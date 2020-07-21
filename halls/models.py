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
    url = models.URLField(max_length=200,default='')
    youtube_id = models.CharField(max_length=255)

    def save(self, hall_id ,force_insert=False, force_update=False, using=None, update_fields=None):
        self.hall = Hall.objects.get(id = hall_id)
        return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

    def __str__(self):
        return self.title