# Generated by Django 4.0.3 on 2022-03-09 05:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_app', '0002_alter_purchaseordergroup_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseordergroup',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('6f0c0dc1-60c4-431a-911f-b681f6fd3180')),
        ),
    ]