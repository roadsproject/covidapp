# Generated by Django 3.0.8 on 2020-10-04 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0003_auto_20200912_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='email',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='visit',
            name='firstname',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='visit',
            name='lastname',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='visit',
            name='phone',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
    ]
