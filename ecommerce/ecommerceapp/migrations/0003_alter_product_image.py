# Generated by Django 5.0.2 on 2024-02-27 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0002_delete_orders_delete_orderupdate_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='images/images'),
        ),
    ]
