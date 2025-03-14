# Generated by Django 5.1.6 on 2025-03-03 02:07

import assidu.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("assidu", "0012_alter_city_area_sq_km"),
    ]

    operations = [
        migrations.AlterField(
            model_name="city",
            name="area_sq_km",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[
                    assidu.models.validate_not_divisible_by_seven,
                    assidu.models.validate_even,
                ],
            ),
        ),
    ]
