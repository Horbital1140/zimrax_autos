# Generated by Django 4.2.8 on 2024-03-01 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_payment_payment_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Manual_payment',
        ),
    ]