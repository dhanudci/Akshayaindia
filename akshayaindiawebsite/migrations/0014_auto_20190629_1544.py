# Generated by Django 2.2.1 on 2019-06-29 15:44

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('akshayaindiawebsite', '0013_auto_20190629_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_content',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=1),
            preserve_default=False,
        ),
    ]
