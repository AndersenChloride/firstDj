# Generated by Django 4.1.7 on 2023-05-19 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_delete_hospstore_delete_pharmdrugs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id_store', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'store',
                'managed': False,
            },
        ),
    ]