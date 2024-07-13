from django.db import models

# Create your models here.

# create class
class Recipe(models.Model):
    #create attributes
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    servings = models.PositiveIntegerField(help_text="Number of servings")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='recipe_images/', blank=True, null=True)

    def __str__(self):
        return self.title