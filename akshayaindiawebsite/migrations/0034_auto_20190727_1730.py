# Generated by Django 2.2.1 on 2019-07-27 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akshayaindiawebsite', '0033_auto_20190727_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacationenquiry',
            name='Class',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='vacationenquiry',
            name='number_of_children',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='vacationenquiry',
            name='number_of_infant',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='vacationenquiry',
            name='travel_mode',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]