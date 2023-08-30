from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='media/tweet_images', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} | {self.description} | {self.datetime}'
