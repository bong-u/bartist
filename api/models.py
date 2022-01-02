from django.db import models

# Create your models here.
class Artist(models.Model):
    
    name = models.CharField(max_length=30)
    value = models.IntegerField(primary_key=True)
    recent = models.IntegerField()
    image = models.URLField()
    
    def __str__(self):
        return self.name