# Generated by Django 4.2.8 on 2023-12-11 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gw2_logs', '0002_instance_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instance',
            name='type',
            field=models.CharField(choices=[('raid', 'Raid'), ('fractal', 'Fractal'), ('strike', 'Strike')], default='raid', max_length=10),
        ),
    ]
