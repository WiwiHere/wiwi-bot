# Generated by Django 4.2.8 on 2023-12-12 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gw2_logs', '0028_instanceclear_instance'),
    ]

    operations = [
        migrations.AddField(
            model_name='instanceclear',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
    ]