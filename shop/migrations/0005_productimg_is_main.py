# Generated by Django 3.0.5 on 2020-04-21 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20200420_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimg',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
    ]
