# Generated by Django 3.0.5 on 2020-04-26 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingCart', '0004_item_itemimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='catagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catName', models.CharField(max_length=100)),
                ('catImage', models.ImageField(upload_to='pictures')),
            ],
        ),
    ]
