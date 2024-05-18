# Generated by Django 4.2.6 on 2024-05-18 07:31

from django.db import migrations, models

from wger.nutrition.models import Source


def set_external_id(apps, schema_editor):
    """Set remote_id, used by imported ingredients (OFF, etc.)"""

    Ingredient = apps.get_model('nutrition', 'Ingredient')
    for ingredient in Ingredient.objects.filter(source_name=Source.OPEN_FOOD_FACTS.value):
        ingredient.remote_id = ingredient.code
        ingredient.save()


class Migration(migrations.Migration):
    dependencies = [
        ('nutrition', '0020_full_text_search'),
    ]

    operations = [
        migrations.RenameIndex(
            model_name='ingredient',
            new_name='nutrition_i_name_8f538f_gin',
            old_name='nutrition_i_search__f274b7_gin',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='remote_id',
            field=models.CharField(blank=True, db_index=True, max_length=200, null=True),
        ),
        migrations.RunPython(
            set_external_id,
            reverse_code=migrations.RunPython.noop,
        ),
    ]
