# Generated by Django 4.1.5 on 2023-01-25 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0012_alter_slot_intent_alter_utterance_intent'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='options',
            field=models.TextField(default='s,m,l'),
            preserve_default=False,
        ),
    ]