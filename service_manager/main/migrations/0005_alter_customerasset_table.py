# Generated by Django 4.1.1 on 2022-09-07 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_customerasset_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='customerasset',
            table='main_customer_assets',
        ),
    ]
