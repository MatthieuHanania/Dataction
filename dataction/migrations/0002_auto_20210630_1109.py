# Generated by Django 3.2.4 on 2021-06-30 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pointgps',
            name='lat',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pointgps',
            name='long',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
