from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RecipeSerializer
from .serializers import NoteSerializer
from rest_framework.decorators import action
from recipe.models import Recipe
from note.models import Note
import uuid


# Create your views here.

class RecipeView(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()


@api_view(['POST'])
def like_recipe(request, recipe_id):
    try:
        print(recipe_id, 'id in like_recipe')
        recipe = get_object_or_404(Recipe, id=recipe_id)
        print(recipe.isLiked, 'recipe.isLiked in like_recipe')
        if recipe.isLiked:
            return Response({'status': 'already liked'}, status=400)
        
        recipe.isLiked = True
        recipe.save()
        print(recipe.isLiked, 'recipe.isLiked after saving')
        return Response({'status': 'liked'})
    
    except Exception as e:
        print(f"Error liking recipe: {e}")
        return Response({'status': 'error'}, status=500)

@api_view(['POST'])
def unlike_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if not recipe.isLiked:
        return Response({'status': 'not liked'}, status=400)
    recipe.isLiked = False
    recipe.save()
    return Response({'status': 'unliked'})

@api_view(['DELETE'])
def delete_recipe(request, recipe_id):
    try:
        recipe = Recipe.objects.get(id=recipe_id)
    except Recipe.DoesNotExist:
        return Response({"error": "Recipe not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['PUT'])
def put_recipe(request, recipe_id):
    try:
        recipe = Recipe.objects.get(id=recipe_id)
    except Recipe.DoesNotExist:
        return Response({"error": "Recipe not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = RecipeSerializer(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

## notes ##
@api_view(['POST'])
def notes(request, recipe_id):
    try:
        if not isinstance(recipe_id, str):
            recipe_id = str(recipe_id)
            
        recipe_uuid = uuid.UUID(recipe_id)
        recipe = Recipe.objects.get(id=recipe_uuid)
    except Recipe.DoesNotExist:
        return Response({"error": "Recipe not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        body = request.data.get('body', '')
        if len(body) > 500:
            return Response({'error': 'Note body exceeds 500 characters.'}, status=status.HTTP_400_BAD_REQUEST)
    
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(recipe=recipe)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def delete_note(request, recipe_id, note_id):
    print(note_id, 'note id')
    try:
        note = Note.objects.get(id=note_id, recipe_id=recipe_id)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Note.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
