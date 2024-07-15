from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RecipeSerializer
from .serializers import NoteSerializer
from recipe.models import Recipe
from note.models import Note


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

@api_view(['POST'])
def notes(request, recipe_id):
    try:
        recipe = Recipe.objects.get(id=recipe_id)
    except Recipe.DoesNotExist:
        return Response({"error": "Recipe not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(recipe=recipe)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)