# Generated by Django 4.1.4 on 2023-01-01 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_alter_payment_options_alter_paymentinstance_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="amount",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="payment",
            name="recipient_email",
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name="payment",
            name="title",
            field=models.CharField(max_length=200, null=True),
        ),
    ]