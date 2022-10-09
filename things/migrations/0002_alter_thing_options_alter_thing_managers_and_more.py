# Generated by Django 4.1.2 on 2022-10-09 12:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='thing',
            options={},
        ),
        migrations.AlterModelManagers(
            name='thing',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='thing',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='thing',
            name='email',
        ),
        migrations.RemoveField(
            model_name='thing',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='thing',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='thing',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='thing',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='thing',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='thing',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='thing',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='thing',
            name='password',
        ),
        migrations.RemoveField(
            model_name='thing',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='thing',
            name='username',
        ),
        migrations.AlterField(
            model_name='thing',
            name='description',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='thing',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='thing',
            name='quantity',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]