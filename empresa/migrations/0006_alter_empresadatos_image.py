# Generated by Django 5.0 on 2023-12-11 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0005_alter_empresadatos_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresadatos',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='projectempresa', verbose_name='Imagen'),
        ),
    ]
