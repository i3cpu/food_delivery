# Generated by Django 4.2.1 on 2023-06-08 11:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('basket', '0009_alter_ordersmodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordersmodel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
