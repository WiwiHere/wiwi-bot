# Generated by Django 4.2.8 on 2024-03-08 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gw2_logs', '0070_remove_encounter_use_total_clear_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encounter',
            name='emoji',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='encounters', to='gw2_logs.emoji'),
        ),
        migrations.AlterField(
            model_name='encounter',
            name='use_in_instance_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='encounters', to='gw2_logs.instancegroup'),
        ),
    ]
