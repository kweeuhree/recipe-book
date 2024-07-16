from django.db import models
import uuid

# Create your models here.

# create class
class Recipe(models.Model):
    #create attributes
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    servings = models.PositiveIntegerField(help_text="Number of servings")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    isLiked = models.BooleanField(default=False)
    image = models.ImageField(upload_to='recipe_images/', blank=True, null=True)

    # Order by date_created in descending order
    class Meta:
        ordering = ['-date_created']  

    def __str__(self):
        return self.title