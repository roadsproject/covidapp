# Generated by Django 3.1.1 on 2020-09-12 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='User_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tracking.user'),
            preserve_default=False,
        ),
    ]
