# Generated by Django 4.2.8 on 2023-12-11 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gw2_logs', '0006_rename_dpslogs_dpslog_rename_raidclears_raidclear'),
    ]

    operations = [
        migrations.RenameField(
            model_name='raidclear',
            old_name='title',
            new_name='name',
        ),
    ]
