# Generated by Django 5.1.6 on 2025-03-05 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("watchlist_app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="movie",
            old_name="activate",
            new_name="active",
        ),
    ]
