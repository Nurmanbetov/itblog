# Generated by Django 3.0.6 on 2020-06-18 13:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20200616_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='photo',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='author_photo'),
            preserve_default=False,
        ),
    ]
