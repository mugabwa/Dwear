# Generated by Django 2.2.12 on 2022-02-03 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='cost',
            field=models.FloatField(default=0.0),
        ),
    ]