# Generated by Django 2.2.1 on 2019-06-29 14:35

import akshayaindiawebsite.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akshayaindiawebsite', '0012_auto_20190628_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallarymodel',
            name='gallary_image',
            field=models.FileField(upload_to=akshayaindiawebsite.models.GallaryModel.gallary_image_path),
        ),
    ]