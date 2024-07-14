from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RecipeSerializer
from .models import Recipe


# Create your views here.

class RecipeView(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()


@api_view(['POST'])
def like_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if recipe.isLiked:
        return Response({'status': 'already liked'}, status=400)
    recipe.isLiked = True
    recipe.save()
    return Response({'status': 'liked'})

@api_view(['POST'])
def unlike_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if not recipe.isLiked:
        return Response({'status': 'not liked'}, status=400)
    recipe.isLiked = False
    recipe.save()
    return Response({'status': 'unliked'})