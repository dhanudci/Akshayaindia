# Generated by Django 2.2.1 on 2019-07-27 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akshayaindiawebsite', '0032_auto_20190726_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacation',
            name='tour_price',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]