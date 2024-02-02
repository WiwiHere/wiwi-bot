# Generated by Django 4.2.8 on 2024-01-26 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gw2_logs', '0057_instancecleargroup_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='instancecleargroup',
            name='type',
            field=models.CharField(choices=[('raid', 'Raid'), ('fractal', 'Fractal'), ('strike', 'Strike')], default='raid', max_length=10),
        ),
    ]