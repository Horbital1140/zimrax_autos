# Generated by Django 4.2.8 on 2024-02-06 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_payment_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alt_pay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acct_name', models.CharField(max_length=50)),
                ('bnk_name', models.CharField(max_length=50)),
                ('acct_number', models.IntegerField()),
            ],
        ),
    ]
