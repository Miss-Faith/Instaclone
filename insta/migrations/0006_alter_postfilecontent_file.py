# Generated by Django 4.0.5 on 2022-06-10 00:21

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0005_recipients_post_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postfilecontent',
            name='file',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='file'),
        ),
    ]
