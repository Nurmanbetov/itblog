# Generated by Django 3.0.6 on 2020-06-23 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0011_auto_20200618_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='articles/20200623'),
        ),
    ]
