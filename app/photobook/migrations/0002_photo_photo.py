# Generated by Django 2.2.9 on 2020-01-17 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photobook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='photo',
            field=models.ImageField(default='', upload_to='images/'),
            preserve_default=False,
        ),
    ]
