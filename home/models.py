from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Blog(models.Model):
    title = models.CharField(max_length=250)
    title_tag = models.CharField(max_length=100)
    content_tag = models.TextField()
    content = models.TextField()
    category = models.CharField(max_length=250)
    created_on = models.DateTimeField(default=datetime.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    published_status = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Blogs'


    def __str__(self):
        return self.title