# Generated by Django 4.1.7 on 2023-02-25 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserMessage', '0002_user_address_user_message_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='message',
            field=models.TextField(blank=True, max_length=225, null=True),
        ),
    ]
