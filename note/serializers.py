from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Note:
        model = Note
        fields = ('id', 'recipe', 'date', 'date_updated', 'body', 'isLiked')