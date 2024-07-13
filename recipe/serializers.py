from rest_framework import serializers
from note.serializers import NoteSerializer 
from recipe.models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    notes = NoteSerializer(many=True, read_only=True)
    class Meta:
        model = Recipe
        fields = ('id', 'title', 'description', 'ingredients', 'instructions', 'servings', 'date_created', 'date_updated', 'image', 'notes')