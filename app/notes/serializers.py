"""Serializer for Notes"""

from rest_framework import serializers
from notes.models import Notes


class NotesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ["title", "body"]
