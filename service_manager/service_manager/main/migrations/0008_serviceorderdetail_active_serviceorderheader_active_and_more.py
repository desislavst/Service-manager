# Generated by Django 4.1.1 on 2022-10-20 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_serviceorderheader_problem_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceorderdetail',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='serviceorderheader',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='serviceordernote',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]