# Generated by Django 4.2.18 on 2025-02-27 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_postpractice"),
    ]

    operations = [
        migrations.CreateModel(
            name="PreMatch",
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
                ("tournament", models.TextField()),
                ("venue", models.TextField()),
                ("date", models.DateTimeField()),
                ("event", models.TextField()),
                ("rounds", models.TextField()),
                ("opponent_name", models.TextField()),
                ("academy", models.TextField()),
                (
                    "playing_hand",
                    models.IntegerField(
                        choices=[(0, "Right-Handed"), (1, "Left-Handed")]
                    ),
                ),
                ("fh_rubber", models.TextField()),
                ("bh_rubber", models.TextField()),
                ("blade", models.TextField()),
                ("strengths", models.TextField()),
                ("weaknesses", models.TextField()),
                ("goals", models.TextField()),
                ("plan", models.TextField()),
                ("warm_up_physical", models.BooleanField(default=False)),
                ("warm_up_mental", models.BooleanField(default=False)),
                ("pmr", models.BooleanField(default=False)),
                ("visualization", models.BooleanField(default=False)),
                ("breathing", models.BooleanField(default=False)),
                ("self_talk", models.BooleanField(default=False)),
                ("keywords", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Skill",
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
                ("player", models.CharField(max_length=50)),
                ("skill_name", models.CharField(max_length=50)),
                ("stroke_type", models.CharField(max_length=255)),
                ("response", models.CharField(max_length=50)),
                ("response_from", models.CharField(max_length=50)),
                ("response_length", models.CharField(max_length=50)),
                ("target_placements", models.JSONField(default=list)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
