# Generated by Django 4.2.8 on 2024-01-26 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gw2_logs', '0058_instancecleargroup_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instancecleargroup',
            name='type',
            field=models.CharField(choices=[('raid', 'Raid'), ('fractal', 'Fractal')], default='raid', max_length=10),
        ),
    ]