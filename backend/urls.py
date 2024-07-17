"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import routers
from .views import home_page
from recipe import views as recipe_views
from note import views as note_views

router = routers.DefaultRouter()
router.register(r'recipes', recipe_views.RecipeView, 'recipe')
router.register(r'notes', note_views.NoteView, 'note')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)), 
    path('api/recipes/<uuid:recipe_id>/like/', recipe_views.like_recipe, name='like_recipe'),
    path('api/recipes/<uuid:recipe_id>/unlike/', recipe_views.unlike_recipe, name='unlike_recipe'),
    path('api/recipes/<uuid:recipe_id>/notes/', recipe_views.notes, name='notes'),
    path('api/recipes/<uuid:recipe_id>', recipe_views.delete_recipe, name='delete_recipe'),
    path('api/recipes/<uuid:recipe_id>', recipe_views.put_recipe, name='put_recipe'),
    path('api/recipes/<uuid:recipe_id>/notes/<int:note_id>/', recipe_views.delete_note, name='recipe-note-delete' ),

    re_path(r'^.*$', home_page),  # Catch-all route
]
# Serve static and media files during development
if settings.DEBUG:
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)