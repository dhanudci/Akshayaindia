# Generated by Django 2.2.1 on 2019-07-29 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akshayaindiawebsite', '0040_auto_20190729_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corporateenquiry',
            name='additional_request',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]