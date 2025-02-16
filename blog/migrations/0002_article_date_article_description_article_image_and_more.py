# Generated by Django 5.1 on 2024-08-13 00:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]
