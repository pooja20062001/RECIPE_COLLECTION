from django.db import models

# Create your models here.
class Recipe(models.Model):
    title=models.CharField(max_length=30)
    ingredients=models.TextField()
    preparation_time=models.TimeField(max_length=100)
    instructions=models.TextField(max_length=200)

    def __str__(self):
        return self.title
