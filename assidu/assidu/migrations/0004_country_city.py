# Generated by Django 5.1.6 on 2025-03-01 09:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("assidu", "0003_alter_accomplishment_notes_alter_task_enddate"),
    ]

    operations = [
        migrations.CreateModel(
            name="Country",
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
                ("country_iso_name", models.CharField(max_length=3)),
                ("population", models.IntegerField()),
                ("area_sq_km", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="City",
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
                ("mayor_name", models.CharField(max_length=255)),
                ("date_of_last_mayoral_election", models.DateField()),
                ("population", models.IntegerField()),
                ("area_sq_km", models.IntegerField()),
                ("elevation_metres", models.IntegerField()),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="assidu.country"
                    ),
                ),
            ],
        ),
    ]
