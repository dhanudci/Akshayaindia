# Generated by Django 2.2.1 on 2019-07-28 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akshayaindiawebsite', '0036_auto_20190727_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelenquiry',
            name='additional_request',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='hotelenquiry',
            name='number_of_children',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='vacationenquiry',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
    ]