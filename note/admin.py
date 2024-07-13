from django.contrib import admin
from .models import Todo

class NoteAdmin(admin.ModelAdmin):
    list_display = ('date', 'body', 'isLiked')

# Register your models here.

admin.site.register(Note, NoteAdmin)