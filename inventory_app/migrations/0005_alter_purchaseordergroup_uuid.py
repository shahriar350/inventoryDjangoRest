# Generated by Django 4.0.3 on 2022-03-12 18:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_app', '0004_alter_purchaseordergroup_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseordergroup',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('8d44ed46-6fd1-4059-9f6a-a2306e2a9d50')),
        ),
    ]
