# Generated by Django 5.1.6 on 2025-03-03 02:02

import assidu.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("assidu", "0011_alter_city_some_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="city",
            name="area_sq_km",
            field=models.IntegerField(
                blank=True, null=True, validators=[assidu.models.divisible_by_seven]
            ),
        ),
    ]
