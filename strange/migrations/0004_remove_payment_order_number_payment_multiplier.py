# Generated by Django 4.0.4 on 2022-05-24 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strange', '0003_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='order_number',
        ),
        migrations.AddField(
            model_name='payment',
            name='multiplier',
            field=models.IntegerField(default=1),
        ),
    ]