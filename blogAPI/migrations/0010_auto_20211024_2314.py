# Generated by Django 3.2.8 on 2021-10-24 15:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blogAPI', '0009_alter_comment_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.AddField(
            model_name='comment',
            name='post_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
