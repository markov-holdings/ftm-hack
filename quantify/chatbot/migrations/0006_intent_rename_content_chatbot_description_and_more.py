# Generated by Django 4.1.5 on 2023-01-16 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0005_remove_chatbot_dataprivacy_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameField(
            model_name='chatbot',
            old_name='content',
            new_name='description',
        ),
        migrations.AddField(
            model_name='chatbot',
            name='aws_bot_id',
            field=models.CharField(default=-1, max_length=50),
        ),
        migrations.AddField(
            model_name='chatbot',
            name='bot_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='chatbot',
            name='locale_status',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Utterance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('intent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='chatbot.intent')),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('intent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='chatbot.intent')),
            ],
        ),
        migrations.AddField(
            model_name='intent',
            name='chatbot',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='chatbot.chatbot'),
        ),
    ]
