# Generated by Django 4.1.3 on 2023-08-27 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0014_professionalexperience_job_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobdescription',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]