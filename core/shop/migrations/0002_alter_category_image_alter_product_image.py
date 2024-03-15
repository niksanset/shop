# Generated by Django 5.0.3 on 2024-03-15 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default='category/default.jpg', upload_to='category/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='product/default.jpg', upload_to='product/'),
        ),
    ]