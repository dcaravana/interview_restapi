# -*- coding: utf-8 -*-

"""This module contains all the tests and related functions."""

from __future__ import unicode_literals

import uuid
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Comment

# Create your tests here.


class CommentModelTestCase(TestCase):
    """This class defines the test suite for the Comment model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.comment_sku = uuid.uuid1()
        self.comment_content = "This is an interesting comment."
        self.comment = Comment(
            sku=self.comment_sku, content=self.comment_content)

    def test_model_can_create_a_comment(self):
        """Test the Comment model can create a comment."""
        old_count = Comment.objects.count()
        self.comment.save()
        new_count = Comment.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_can_do_tone(self):
        """Test the Comment model calls sentiment analysis service."""
        self.comment.save()
        self.assertNotEqual(self.comment.tone, '')


class CommentViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()

        user = User.objects.create_superuser('admin', 'admin@none.no', 'admin')
        self.client.force_authenticate(user=user)

        self.commment_data = {
            'sku': uuid.uuid1(),
            'content': "This is an interesting comment."
        }

        self.response = self.client.post(
            '/comments/',
            self.commment_data,
            format="json")

    def test_api_can_create_a_comment(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
