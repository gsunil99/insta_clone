# Generated by Django 3.1.3 on 2021-07-14 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20210714_1031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='account',
        ),
        migrations.AddField(
            model_name='user',
            name='is_private_account',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True),
            preserve_default=False,
        ),
    ]
