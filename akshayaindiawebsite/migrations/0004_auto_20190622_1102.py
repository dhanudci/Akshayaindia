# Generated by Django 2.2.1 on 2019-06-22 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akshayaindiawebsite', '0003_itinerarysectionmodel_description1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itinerarysectionmodel',
            name='description1',
        ),
        migrations.AlterField(
            model_name='itinerarysectionmodel',
            name='description',
            field=models.TextField(),
        ),
    ]