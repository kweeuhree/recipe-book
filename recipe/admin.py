from django.contrib import admin
from .models import Recipe

class RecipeAdmin(admin.ModelAdmin):
        list_display = ('title', 'description', 'ingredients', 'date_created', 'date_updated')
        list_filter = ('date_created', 'date_updated')

# Register your models here.
admin.site.register(Recipe, RecipeAdmin)