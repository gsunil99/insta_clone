# Generated by Django 3.1.3 on 2021-06-26 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210624_2244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follow',
            name='is_follow',
        ),
    ]
