# Generated by Django 4.1.4 on 2022-12-14 09:45

from django.db import migrations
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_user_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', user.models.UserManager()),
            ],
        ),
    ]
