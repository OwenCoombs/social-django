# Generated by Django 5.0.6 on 2024-06-06 17:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_image_upload', '0006_alter_image_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='profile',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app_image_upload.profile'),
        ),
    ]
