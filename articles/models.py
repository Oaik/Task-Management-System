from django.db import models
from django import forms
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    startDate = models.DateField(blank=True)
    endDate = models.DateField(blank=True)
    author = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'
