# Generated by Django 4.1.4 on 2023-01-13 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0015_paymentmethod_stripe_account_id_alter_payment_user_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="paymentmethod",
            name="stripe_payment_method_id",
            field=models.CharField(max_length=200, null=True),
        ),
    ]
