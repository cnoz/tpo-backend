# Generated by Django 5.0 on 2023-12-17 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0011_alter_empresadatos_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresadatos',
            name='email',
            field=models.EmailField(blank=True, default='none@tumail.com', max_length=30, null=True, verbose_name='Correo de contacto.'),
        ),
    ]
