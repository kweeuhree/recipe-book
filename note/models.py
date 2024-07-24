from django.db import models
from recipe.models import Recipe
from django.utils import timezone

def get_default_date_created():
    return timezone.now()

# Create your models here.
class Note(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='notes', null=True, blank=True)
    date_created = models.DateTimeField(default=get_default_date_created)
    date_updated = models.DateTimeField(auto_now=True)
    body = models.TextField(max_length=500)
    isLiked = models.BooleanField(default=False)

    def __str__(self):
        return f'Note for {self.recipe} - {self.date_created}'
    # return body of the note
    def returnBody(self):
        return self.body
