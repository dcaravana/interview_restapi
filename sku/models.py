# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from watson_developer_cloud import ToneAnalyzerV3
import json
from django.conf import settings

# Create your models here.


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    sku = models.CharField(max_length=100, blank=False)
    content = models.TextField()
    tone = models.TextField(blank=True)
    # user

    class Meta:
        ordering = ('created',)


# alternative: create a ToneField with pre_save()
@receiver(pre_save, sender=Comment)
def provide_tone(sender, instance, *args, **kwargs):
    
    # TODO move outside to get a singleton?
    tone_analyzer = ToneAnalyzerV3(
        username=settings.WATSON_USERNAME,
        password=settings.WATSON_PASSWORD,
        version='2016-05-19')
    
    # TODO manage error properly
    tone = tone_analyzer.tone(text=instance.content)
    
    instance.tone = json.dumps(tone)
