# Generated by Django 4.2.8 on 2023-12-12 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gw2_logs', '0031_rename_raidclear_instancecleargroup_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instancecleargroup',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]