# Generated by Django 3.0.5 on 2020-05-01 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userAccess', '0004_user_last_login'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user',
        ),
    ]
