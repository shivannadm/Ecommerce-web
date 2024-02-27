# Generated by Django 5.0.2 on 2024-02-27 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Orders',
        ),
        migrations.DeleteModel(
            name='OrderUpdate',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default_image.jpg', upload_to='images/images'),
        ),
    ]