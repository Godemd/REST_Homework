# Generated by Django 5.1.3 on 2024-12-09 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_user_options_payment"),
    ]

    operations = [
        migrations.RenameField(
            model_name="payment",
            old_name="date",
            new_name="created_at",
        ),
        migrations.RenameField(
            model_name="payment",
            old_name="payment_method",
            new_name="method",
        ),
    ]
