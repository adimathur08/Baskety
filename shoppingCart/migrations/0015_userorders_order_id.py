# Generated by Django 3.0.5 on 2020-05-08 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingCart', '0014_remove_userorders_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='userorders',
            name='order_id',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]