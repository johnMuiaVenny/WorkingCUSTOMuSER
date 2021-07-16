from django.db import models
from django.urls import reverse

# Create your models here.

class COMMENTT(models.Model):
    Picture = models.FileField(upload_to='images')
    Title = models.CharField(max_length = 100)
    Description = models.TextField()

    def get_absolute_url(self):
        return reverse('COMMENTS:Comment', kwargs={'pk':self.pk})    

    def __str__(self):
        return self.Title