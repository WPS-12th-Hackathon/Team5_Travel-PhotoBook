# Generated by Django 2.2.9 on 2020-01-17 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photobook', '0003_auto_20200117_1437'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='pagenumber',
        ),
    ]
