# Generated by Django 3.0 on 2020-11-19 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CharitySystem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation_request',
            name='connector',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='CharitySystem.NGO'),
            preserve_default=False,
        ),
    ]
