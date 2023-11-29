# Generated by Django 2.2.1 on 2019-07-11 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akshayaindiawebsite', '0019_auto_20190706_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itinerarysectionmodel',
            name='breakfast',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='itinerarysectionmodel',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='itinerarysectionmodel',
            name='dinner',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='itinerarysectionmodel',
            name='heading',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='itinerarysectionmodel',
            name='lunch',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='itinerarysectionmodel',
            name='stay_in_hotel',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
