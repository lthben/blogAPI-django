# Generated by Django 3.2.8 on 2021-10-24 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogAPI', '0006_auto_20211024_1826'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='temp_id',
            new_name='id',
        ),
    ]
