# Generated by Django 2.2.1 on 2019-07-15 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akshayaindiawebsite', '0026_auto_20190714_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacation',
            name='services',
            field=models.TextField(blank=True, null=True),
        ),
    ]
