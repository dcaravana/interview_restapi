# -*- coding: utf-8 -*-
"""This module contains all the models and related functions."""

from __future__ import unicode_literals

import json
import logging
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from watson_developer_cloud import ToneAnalyzerV3  # pylint: disable=import-error

# Create your models here.

LOGGER = logging.getLogger('django')


class Comment(models.Model):
    """Comment is the main app entity."""
    created = models.DateTimeField(auto_now_add=True)
    sku = models.CharField(max_length=100, blank=False)
    content = models.TextField()
    tone = models.TextField(blank=True)
    # TODO user

    # Implemented through a dynamic property and this is probably not necessary
    # here or even bad performance-wise, but it's an example of calculated
    # field.
    @property
    def tone_is_positive(self):
        """Returns whether the comment sentiment is positive."""

        if not self.tone:
            return None

        # this should never break
        try:
            tone = json.loads(self.tone)
            tone_categories = tone['document_tone']['tone_categories']

            joy = 0.0
            for tone_category in tone_categories:
                if tone_category['category_id'] == 'emotion_tone':
                    for tone_category_tone in tone_category['tones']:
                        if tone_category_tone['tone_id'] == 'joy':
                            joy = tone_category_tone['score']

            return joy >= 0.5
        except:  # pylint: disable=bare-except
            LOGGER.exception('Problem with tone JSON data.')

    class Meta(object):
        """Comments are currently ordered by creation date."""
        ordering = ('created',)


# alternative: create a ToneField with pre_save()
@receiver(pre_save, sender=Comment)
def provide_tone(sender, instance, *args, **kwargs):
    """Calls the tone analysis service just before saving the new record."""

    # TODO manage error properly
    try:

        # TODO move outside to get a singleton? multi-thread safe?
        tone_analyzer = ToneAnalyzerV3(
            username=settings.WATSON_USERNAME,
            password=settings.WATSON_PASSWORD,
            version='2016-05-19')

        tone = tone_analyzer.tone(text=instance.content)

        instance.tone = json.dumps(tone)

    except:
        LOGGER.exception('Problem with tone Watson call.')
