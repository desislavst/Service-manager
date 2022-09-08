# Generated by Django 4.1.1 on 2022-09-08 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_employee_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaterialCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ServiceOrderHeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('serviced_on', models.DateTimeField(blank=True, null=True)),
                ('completed_on', models.DateTimeField(blank=True, null=True)),
                ('accepted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accepted_by', to='main.employee')),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.asset')),
                ('completed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='completed_by', to='main.employee')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.customer')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.customerdepartment')),
                ('serviced_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='serviced_by', to='main.employee')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.materialcategory')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]