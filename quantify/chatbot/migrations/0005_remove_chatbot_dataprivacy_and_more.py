# Generated by Django 4.1.5 on 2023-01-14 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0004_chatbot_dataprivacy_chatbot_idlesessionttlinseconds_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatbot',
            name='dataPrivacy',
        ),
        migrations.RemoveField(
            model_name='chatbot',
            name='idleSessionTTLInSeconds',
        ),
        migrations.RemoveField(
            model_name='chatbot',
            name='roleArn',
        ),
    ]