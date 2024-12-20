# Generated by Django 3.2.25 on 2024-12-16 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredient', '0003_auto_20241214_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientitem',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='recipeitem',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='recipeitem',
            name='list_ingredient',
            field=models.ManyToManyField(to='ingredient.IngredientItem'),
        ),
    ]
