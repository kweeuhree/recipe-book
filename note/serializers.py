from rest_framework import serializers
from note.models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'recipe', 'date_created', 'date_updated', 'body', 'isLiked')

