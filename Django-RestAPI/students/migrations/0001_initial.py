# Generated by Django 5.2 on 2025-04-22 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
            ],
        ),
    ]
