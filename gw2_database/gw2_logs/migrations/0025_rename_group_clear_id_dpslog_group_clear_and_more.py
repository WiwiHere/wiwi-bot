# Generated by Django 4.2.8 on 2023-12-12 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gw2_logs', '0024_dpslog_success'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dpslog',
            old_name='group_clear_id',
            new_name='group_clear',
        ),
        migrations.RenameField(
            model_name='dpslog',
            old_name='instance_clear_id',
            new_name='instance_clear',
        ),
    ]