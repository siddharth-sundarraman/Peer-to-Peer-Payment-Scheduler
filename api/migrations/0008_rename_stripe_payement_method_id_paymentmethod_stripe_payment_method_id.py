# Generated by Django 4.1.4 on 2023-01-05 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0007_paymentmethod_title"),
    ]

    operations = [
        migrations.RenameField(
            model_name="paymentmethod",
            old_name="stripe_payement_method_id",
            new_name="stripe_payment_method_id",
        ),
    ]
