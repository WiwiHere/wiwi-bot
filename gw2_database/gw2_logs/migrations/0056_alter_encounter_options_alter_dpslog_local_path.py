# Generated by Django 4.2.8 on 2024-01-26 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gw2_logs', '0055_instanceclear_emboldened'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='encounter',
            options={'ordering': ['instance', 'nr']},
        ),
        migrations.AlterField(
            model_name='dpslog',
            name='local_path',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]