# Generated by Django 4.1.5 on 2023-01-14 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0003_rename_user_chatbot_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatbot',
            name='dataPrivacy',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='chatbot',
            name='idleSessionTTLInSeconds',
            field=models.IntegerField(default=300),
        ),
        migrations.AddField(
            model_name='chatbot',
            name='roleArn',
            field=models.CharField(default='null', max_length=50),
        ),
    ]
