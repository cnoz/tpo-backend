# Generated by Django 5.0 on 2023-12-11 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariodatos',
            name='image',
            field=models.ImageField(null=True, upload_to='datosusuarios', verbose_name='imagen'),
        ),
    ]
