# Generated by Django 3.2.8 on 2021-10-24 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogAPI', '0003_auto_20211024_1825'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='temp_id',
            new_name='id',
        ),
    ]
