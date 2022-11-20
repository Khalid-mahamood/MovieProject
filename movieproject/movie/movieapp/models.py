from django.db import models


# Create your models here.
class Movie(models.Model):
    Name = models.CharField(max_length=250)
    Des = models.TextField()
    Year = models.IntegerField()
    img= models.ImageField(upload_to='Poster')

    def __str__(self):
        return self.Name
