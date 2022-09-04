from django.db import models

# Create your models here.
class Tweets_Model(models.Model):
    tweet = models.CharField(max_length=280)
    username = models.CharField(max_length=15)
