# Generated by Django 3.0.5 on 2020-05-08 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingCart', '0013_orderdetails_userorders'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userorders',
            name='order_id',
        ),
    ]
