# Generated by Django 4.1.1 on 2022-11-14 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_serviceorderdetail_active_serviceorderheader_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceorderheader',
            name='send_emails',
            field=models.BooleanField(default=True),
        ),
    ]
