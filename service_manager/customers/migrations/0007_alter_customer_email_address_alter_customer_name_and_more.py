# Generated by Django 4.1.1 on 2022-11-17 08:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0006_alter_customerrepresentative_email_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email_address',
            field=models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator], verbose_name='email_address'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=20, verbose_name='phone_number'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='vat',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='vat'),
        ),
    ]
