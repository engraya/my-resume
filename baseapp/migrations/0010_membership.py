# Generated by Django 4.1.3 on 2023-08-27 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0009_techskills'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('issuing_body', models.CharField(blank=True, max_length=200, null=True)),
                ('issuing_year', models.CharField(blank=True, max_length=200, null=True)),
                ('membership_id', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
