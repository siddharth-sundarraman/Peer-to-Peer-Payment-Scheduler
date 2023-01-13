# Generated by Django 4.1.4 on 2023-01-03 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_remove_paymentinstance_recipient_has_account_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="paymentinstance",
            name="recurrence",
            field=models.CharField(
                choices=[
                    ("daily", "Daily"),
                    ("weekly", "Weekly"),
                    ("monthly", "Monthly"),
                    ("never", "Never"),
                ],
                max_length=200,
            ),
        ),
    ]