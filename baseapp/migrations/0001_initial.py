# Generated by Django 4.1.3 on 2023-08-23 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=100, null=True)),
                ('profession', models.CharField(blank=True, max_length=200, null=True)),
                ('date_of_birth', models.DateField()),
                ('age', models.IntegerField()),
                ('phone_Number', models.CharField(blank=True, max_length=100, null=True)),
                ('nationality', models.CharField(blank=True, max_length=200, null=True)),
                ('state', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('about_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('year_acquired', models.DateField()),
                ('provider', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('portfolio_description', models.TextField()),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='captions')),
            ],
        ),
        migrations.CreateModel(
            name='ProfessionalExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(blank=True, max_length=200, null=True)),
                ('starting_date', models.DateField()),
                ('ending_date', models.DateField()),
                ('work_place', models.CharField(blank=True, max_length=200, null=True)),
                ('job_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Refree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('profession', models.CharField(blank=True, max_length=100, null=True)),
                ('work_place', models.CharField(blank=True, max_length=200, null=True)),
                ('telephone', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone1', models.CharField(blank=True, max_length=200, null=True)),
                ('phone2', models.CharField(blank=True, max_length=200, null=True)),
                ('email1', models.EmailField(blank=True, max_length=200, null=True)),
                ('email2', models.EmailField(blank=True, max_length=200, null=True)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('github', models.URLField(blank=True, null=True)),
                ('showcase', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Caption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio_shot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baseapp.portfolio')),
            ],
        ),
    ]
