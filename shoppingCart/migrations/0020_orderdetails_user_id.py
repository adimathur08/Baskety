# Generated by Django 3.0.5 on 2020-05-08 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingCart', '0019_auto_20200509_0213'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetails',
            name='user_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
