# Generated by Django 5.0.2 on 2024-02-29 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_remove_room_online_chatmessages_delete_message_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessages',
            name='sender',
            field=models.CharField(max_length=255),
        ),
    ]
