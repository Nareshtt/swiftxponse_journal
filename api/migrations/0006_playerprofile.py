# Generated by Django 4.2.18 on 2025-02-27 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_match_postmatch_game"),
    ]

    operations = [
        migrations.CreateModel(
            name="PlayerProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("player_name", models.CharField(max_length=50)),
                ("academy", models.CharField(max_length=50)),
                (
                    "playing_hand",
                    models.IntegerField(
                        choices=[(0, "Right-Handed"), (1, "Left-Handed")]
                    ),
                ),
                ("fh_rubber", models.CharField(max_length=50)),
                ("bh_rubber", models.CharField(max_length=50)),
                ("blade", models.CharField(max_length=50)),
                ("strength_technical", models.TextField()),
                ("strength_tactical", models.TextField()),
                ("strength_mental", models.TextField()),
                ("weakness_technical", models.TextField()),
                ("weakness_tactical", models.TextField()),
                ("weakness_mental", models.TextField()),
                ("tactics", models.TextField()),
                ("points_scoring", models.TextField()),
                ("points_losing", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
