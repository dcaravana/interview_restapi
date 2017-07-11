"""This module contains all the serializers and related functions."""

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from sku.models import Comment


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for model User."""

    class Meta(object):
        """Only some User attributes are serialized."""
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for model Group."""

    class Meta(object):
        """Only some Group attributes are serialized."""
        model = Group
        fields = ('url', 'name')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for model Comment."""

    class Meta(object):
        """All Comment attributes are currently serialized."""
        model = Comment
        fields = ('created', 'sku', 'content', 'tone', 'tone_is_positive')
