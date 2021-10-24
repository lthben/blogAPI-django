# Generated by Django 3.2.8 on 2021-10-24 10:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blogAPI', '0005_comment_temp_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='id',
        ),
        migrations.AlterField(
            model_name='comment',
            name='temp_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
