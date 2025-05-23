# Generated by Django 5.0.4 on 2025-04-21 21:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0006_product_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categoryId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='category.category'),
        ),
    ]
