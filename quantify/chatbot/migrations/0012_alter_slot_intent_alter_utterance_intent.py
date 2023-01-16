# Generated by Django 4.1.5 on 2023-01-16 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0011_alter_slot_intent_alter_utterance_intent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='intent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='slots', to='chatbot.intent'),
        ),
        migrations.AlterField(
            model_name='utterance',
            name='intent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='utterances', to='chatbot.intent'),
        ),
    ]
