# Generated by Django 4.1.7 on 2023-05-19 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_delete_schedule'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HospStore',
        ),
        migrations.DeleteModel(
            name='PharmDrugs',
        ),
    ]
