# Generated by Django 4.0.3 on 2022-03-09 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='opening_due',
        ),
        migrations.AddField(
            model_name='userdetails',
            name='due',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='due_update',
            field=models.DateField(blank=True, null=True),
        ),
    ]
