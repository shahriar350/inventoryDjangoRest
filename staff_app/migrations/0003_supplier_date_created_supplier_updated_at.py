# Generated by Django 4.0.3 on 2022-03-09 05:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('staff_app', '0002_rename_previous_due_supplier_due'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supplier',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
