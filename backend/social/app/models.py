# Developed by Vitaly Sem

from django.contrib.auth.models import AbstractUser
from django.db import models


class SocialUser(AbstractUser, models.Model):

    @property
    def fullname(self):
        return self.get_full_name()

    def __unicode__(self):
        return self.fullname


class Post(models.Model):
    user = models.ForeignKey(SocialUser, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=250, unique=True)
    text = models.TextField()
    added = models.DateTimeField(auto_now_add=True)

    liked = models.IntegerField(default=0)
    disliked = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title
