from django.db import models
# from django.shortcuts import reverse
# Create your models here.


class Recipe(models.Model):

    name = models.CharField(max_length=50)
    cooking_time = models.IntegerField(help_text='In Minutes')
    ingredients = models.CharField(
        max_length=255, help_text='Ingredients must be separated by commas.')
    description = models.TextField()
    pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')

    # def get_absolute_url(self):
    #     return reverse('books:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.name)
