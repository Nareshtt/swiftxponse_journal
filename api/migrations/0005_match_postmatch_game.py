# Generated by Django 4.2.18 on 2025-02-27 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_rename_response_skill_placement_from_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Match",
            fields=[
                ("match_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "num_sets",
                    models.IntegerField(
                        choices=[
                            (1, "Best of 1"),
                            (3, "Best of 3"),
                            (5, "Best of 5"),
                            (7, "Best of 7"),
                        ]
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="PostMatch",
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
                ("plans", models.TextField()),
                ("feed_physical", models.TextField()),
                ("feed_mental", models.TextField()),
                ("feed_technical", models.TextField()),
                ("feed_tactical", models.TextField()),
                ("improve_physical", models.TextField()),
                ("improve_mental", models.TextField()),
                ("improve_technical", models.TextField()),
                ("improve_tactical", models.TextField()),
                ("done_better", models.TextField()),
                ("lessons", models.TextField()),
                ("notes", models.TextField()),
                ("player1", models.CharField(max_length=50)),
                ("player2", models.CharField(max_length=50)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "match",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="post_match",
                        to="api.match",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Game",
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
                ("set_number", models.IntegerField()),
                ("player1_score", models.IntegerField()),
                ("player2_score", models.IntegerField()),
                (
                    "match",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="games",
                        to="api.match",
                    ),
                ),
            ],
        ),
    ]
