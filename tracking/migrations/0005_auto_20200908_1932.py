# Generated by Django 2.0.1 on 2020-09-08 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0004_merge_20200908_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='individual',
            name='password',
            field=models.CharField(default=0, max_length=32),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='individual',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]