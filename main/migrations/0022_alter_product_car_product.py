# Generated by Django 4.2.8 on 2024-03-04 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_alter_product_car_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='car_product',
            field=models.CharField(max_length=50),
        ),
    ]