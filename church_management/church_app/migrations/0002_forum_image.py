# Generated by Django 3.0.6 on 2020-06-09 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('church_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='image',
            field=models.ImageField(default=None, upload_to='post_images'),
        ),
    ]
