# Generated by Django 4.2.8 on 2024-03-01 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alt_pay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]