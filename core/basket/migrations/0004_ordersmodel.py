# Generated by Django 4.2.1 on 2023-06-07 15:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0003_alter_menumodel_image_alter_restaurantsmodel_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('basket', '0003_remove_basketmodel_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('product', models.ManyToManyField(related_name='ordered_products', to='foods.menumodel')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
