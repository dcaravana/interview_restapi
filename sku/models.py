# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    sku = models.CharField(max_length=100, blank=False)
    content = models.TextField()

    class Meta:
        ordering = ('created',)
