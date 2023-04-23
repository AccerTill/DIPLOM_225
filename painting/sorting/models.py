from django.db import models
from django.contrib.auth.models import User



class Sorting(models.Model):
    name         = models.CharField(max_length=100)
    genre_author = models.CharField(max_length=500)
    picture      = models.ImageField(upload_to ='sorting/images/')
    links        = models.URLField(blank=True)  # -----links

    def __str__(self):
        return self.name




class Shop(models.Model):
    name         = models.CharField(max_length=100)
    picture      = models.ImageField(upload_to ='sorting/images/')
    author       = models.CharField(max_length=100)
    genre        = models.CharField(max_length=100)
    size         = models.CharField(max_length=30)
    price        = models.CharField(max_length=30)
    # links = models.URLField(blank=True)  # -----links

    def __str__(self):
        return self.name




class Feedbackall(models.Model):
    name         = models.CharField(max_length=100)
    text         = models.TextField(blank=True)
    created      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
