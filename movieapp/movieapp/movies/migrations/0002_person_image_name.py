# Generated by Django 4.2 on 2023-05-19 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='image_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
