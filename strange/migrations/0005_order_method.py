# Generated by Django 4.0.4 on 2022-05-24 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('strange', '0004_remove_payment_order_number_payment_multiplier'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='method',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='strange.payment'),
        ),
    ]
