from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    follows = models.ManyToManyField("User", blank=True, related_name="followers")

class Post(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="posts")
    content = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    like = models.ManyToManyField("User", blank=True, related_name="liked")

    def timestampOfPost(self):
        return self.timestamp.strftime("%b %d %Y, %I:%M %p")

    def __str__(self):
        return f"{self.id}"