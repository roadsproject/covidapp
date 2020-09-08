# Generated by Django 2.0.1 on 2020-09-08 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0005_auto_20200908_1932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='individual',
            name='phone',
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]