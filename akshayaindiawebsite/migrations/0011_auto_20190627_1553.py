# Generated by Django 2.2.1 on 2019-06-27 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akshayaindiawebsite', '0010_auto_20190625_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typesofvisa',
            name='entry',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='typesofvisa',
            name='fees',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='typesofvisa',
            name='processing_time',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='typesofvisa',
            name='stay_period',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='typesofvisa',
            name='validity',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='typesofvisa',
            name='visa_name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
