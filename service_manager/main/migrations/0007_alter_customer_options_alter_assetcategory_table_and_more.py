# Generated by Django 4.1.1 on 2022-09-07 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_customer_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={},
        ),
        migrations.AlterModelTable(
            name='assetcategory',
            table='main_asset_category',
        ),
        migrations.AlterModelTable(
            name='customerasset',
            table='main_customer_asset',
        ),
        migrations.AlterModelTable(
            name='customerdepartment',
            table='main_customer_department',
        ),
        migrations.AlterModelTable(
            name='customerrepresentative',
            table='main_customer_representative',
        ),
        migrations.AlterModelTable(
            name='customertype',
            table='main_customer_type',
        ),
    ]
