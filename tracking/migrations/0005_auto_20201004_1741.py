# Generated by Django 3.0.8 on 2020-10-04 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0004_auto_20201004_1726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visit',
            name='email',
        ),
        migrations.RemoveField(
            model_name='visit',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='visit',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='visit',
            name='phone',
        ),
    ]
