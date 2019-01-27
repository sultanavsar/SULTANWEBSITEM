from django.db import models
from django.utils import timezone
class Post (models.Model):
    yazar = models.ForeignKey('auth.User',on_delete= models.CASCADE)
    baslik = models.CharField(max_length=200)
    metin = models.TextField()
    olus_tar = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.baslik
        

# Create your models here.
