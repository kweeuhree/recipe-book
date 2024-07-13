from django.db import models
from recipe.models import Recipe

# Create your models here.
class Note(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='notes', null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    body = models.TextField(max_length=300)
    isLiked = models.BooleanField(default=False)

    def __str__(self):
        return f'Note for {self.recipe.title} - {self.date_created}'
    # return body of the note
    def returnBody(self):
        return self.body
