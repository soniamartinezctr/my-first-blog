from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title= models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title


#Post nombre de nuestro modelo
#class definiendo un objeto
#models.Model significa que Post es un modelo de Django, así Django sabe que debe guadarlo en la DB
#models.charfield..etc: so n los tipos de campos
#modelos.Foreignkey es una relación (link) con otro modelo