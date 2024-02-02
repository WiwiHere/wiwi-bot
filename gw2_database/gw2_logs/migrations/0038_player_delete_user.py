# Generated by Django 4.2.8 on 2023-12-15 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gw2_logs', '0037_guild_alter_user_guild'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('gw2_id', models.CharField(blank=True, max_length=100, null=True)),
                ('guild', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='players', to='gw2_logs.guild')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]