# Generated by Django 4.2.2 on 2023-06-17 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='register',
            name='email',
        ),
        migrations.RemoveField(
            model_name='register',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='register',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='register',
            name='password',
        ),
        migrations.RemoveField(
            model_name='register',
            name='username',
        ),
        migrations.AlterModelTable(
            name='register',
            table='shared_table_name',
        ),
    ]