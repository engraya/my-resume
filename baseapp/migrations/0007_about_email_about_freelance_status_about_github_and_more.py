# Generated by Django 4.1.3 on 2023-08-24 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0006_rename_email_contact_email1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='freelance_status',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='github',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='qualification',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
