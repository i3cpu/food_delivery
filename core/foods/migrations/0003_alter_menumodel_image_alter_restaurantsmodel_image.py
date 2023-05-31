# Generated by Django 4.2.1 on 2023-05-30 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0002_menumodel_image_restaurantsmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menumodel',
            name='image',
            field=models.ImageField(blank=True, default='images/default.webp', null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='restaurantsmodel',
            name='image',
            field=models.ImageField(blank=True, default='images/default.webp', null=True, upload_to='images'),
        ),
    ]
