import os

from django.db import models
from django.conf import settings

from writing.models import Writing

# Create your models here.
class Comment(models.Model):
    post_id = models.ForeignKey("writing.Writing", on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    inittime = models.DateTimeField(auto_now=True)

