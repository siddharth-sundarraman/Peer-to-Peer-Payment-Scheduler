# Generated by Django 4.1.4 on 2023-01-11 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0010_remove_paymentinstance_task_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="paymentinstance",
            name="recurrence",
        ),
    ]