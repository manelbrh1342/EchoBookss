# Generated by Django 5.1.2 on 2024-11-07 15:56

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='/staticfiles/media/Found, Gabby Skeldon (book I).png', upload_to=core.models.image_upload),
        ),
    ]
