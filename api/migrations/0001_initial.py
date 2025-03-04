# Generated by Django 4.2.18 on 2025-02-27 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PrePractice",
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
                ("objective", models.TextField()),
                ("motivation", models.IntegerField()),
                ("energy_level", models.IntegerField()),
                ("nutrition", models.IntegerField()),
                ("sleep_quality", models.IntegerField()),
                ("stress", models.IntegerField()),
                ("technical", models.TextField()),
                ("tactical", models.TextField()),
                ("physical", models.TextField()),
                ("mental", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Stroke",
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
                ("stroke_name", models.CharField(max_length=255)),
                ("response", models.CharField(max_length=50)),
                ("response_from", models.CharField(max_length=50)),
                ("response_length", models.CharField(max_length=50)),
                ("placement", models.CharField(max_length=50)),
                ("placement_length", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Drill",
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
                ("drill_name", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("strokes", models.ManyToManyField(to="api.stroke")),
            ],
        ),
    ]
