# Generated by Django 4.2.18 on 2025-02-27 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_prematch_skill"),
    ]

    operations = [
        migrations.RenameField(
            model_name="skill",
            old_name="response",
            new_name="placement_from",
        ),
        migrations.RenameField(
            model_name="skill",
            old_name="response_from",
            new_name="placement_length",
        ),
        migrations.RemoveField(
            model_name="skill",
            name="response_length",
        ),
    ]
