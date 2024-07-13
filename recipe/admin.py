from django.contrib import admin
from .models import Recipe

class RecipeAdmin(admin.ModelAdmin):
        list_display = ('title', 'author', 'date_created', 'date_updated')
        search_fields = ('title', 'author')
        list_filter = ('date_created', 'date_updated')

# Register your models here.
admin.site.register(Recipe, RecipeAdmin)