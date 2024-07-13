from django.db import models

# Create your models here.
class Note(models.Model):
    date = models.DateField()
    body = models.TextField(max_length=300)
    isLiked = models.BooleanField(default=False)

    def _str_(self):
        return self.body
