# Generated by Django 2.2.7 on 2019-12-23 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20191223_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secretsanta',
            name='player',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='secretsanta',
            name='santa',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]