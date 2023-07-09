# Generated by Django 4.2.1 on 2023-06-08 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0004_ordersmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordersmodel',
            name='adress',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ordersmodel',
            name='messages',
            field=models.TextField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ordersmodel',
            name='payment_method',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ordersmodel',
            name='status',
            field=models.CharField(default=2, max_length=250),
            preserve_default=False,
        ),
    ]
