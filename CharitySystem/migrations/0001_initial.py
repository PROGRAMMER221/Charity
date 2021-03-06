# Generated by Django 3.0 on 2020-11-19 15:30

from django.db import migrations, models
import django_currentuser.middleware


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='donation_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donar_name', models.CharField(max_length=50)),
                ('donatedTO', models.CharField(max_length=100)),
                ('when', models.DateTimeField()),
                ('amount', models.IntegerField()),
                ('terms', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='donation_request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donation_description', models.TextField(blank=True, default=None)),
                ('donation_amount', models.CharField(blank=True, default=None, max_length=15)),
                ('donation_request_user', models.CharField(blank=True, default=django_currentuser.middleware.get_current_authenticated_user, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='NGO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngo_name', models.CharField(blank=True, max_length=30)),
                ('domain', models.CharField(blank=True, max_length=20)),
                ('head_of_ngo', models.CharField(blank=True, max_length=30)),
                ('contactNo', models.CharField(blank=True, max_length=10)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('address1', models.TextField(max_length=200)),
                ('address2', models.TextField(blank=True, max_length=200)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('registration_cerificate_Trust_Society', models.FileField(blank=True, upload_to='verification')),
                ('certificate_12A', models.FileField(blank=True, upload_to='verification')),
                ('beneficiary_profiles', models.FileField(blank=True, upload_to='verification')),
                ('verification_status', models.NullBooleanField(default=None)),
                ('ngo_current_user', models.CharField(blank=True, default=django_currentuser.middleware.get_current_authenticated_user, max_length=40)),
            ],
        ),
    ]
