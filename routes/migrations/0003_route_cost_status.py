# Generated by Django 2.2.12 on 2022-03-31 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0002_auto_20220330_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='cost_status',
            field=models.BooleanField(default=False),
        ),
    ]
