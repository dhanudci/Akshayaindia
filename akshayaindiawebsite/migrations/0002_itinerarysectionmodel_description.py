# Generated by Django 2.2.1 on 2019-06-21 17:39

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('akshayaindiawebsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itinerarysectionmodel',
            name='description',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
    ]