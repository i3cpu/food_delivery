# Generated by Django 4.2.1 on 2023-06-06 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basketmodel',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]