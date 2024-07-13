from django.db import models

# Create your models here.
class Note(models.Model):
    date = models.DateField(max_length=120)
    body = models.TextField()
    isLiked = models.BooleanField(default=False)

    def _str_(self):
        return self.title
