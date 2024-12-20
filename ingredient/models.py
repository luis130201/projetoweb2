from django.db import models

class IngredientItem(models.Model):
  name = models.TextField()
  property = models.TextField()
  img_url = models.TextField()

class RecipeItem(models.Model):
  name = models.TextField()
  ingredients = models.TextField()
  directions = models.TextField()
  img_url = models.ImageField(upload_to='recipes/', blank=True, null=True)  # Campo de imagem
  list_ingredient = models.ManyToManyField(IngredientItem)
  def __str__(self):
        return self.name