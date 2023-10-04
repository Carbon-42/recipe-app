from django.db import models

# Create your models here.


class Recipe(models.Model):

    name = models.CharField(max_length=50)
    cooking_time = models.IntegerField(help_text='In Minutes')
    ingredients = models.CharField(
        max_length=255, help_text='Ingredients must be separated by commas.')

    def __str__(self):
        return str(self.name)