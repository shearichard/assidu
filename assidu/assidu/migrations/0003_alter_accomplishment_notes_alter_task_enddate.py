# Generated by Django 5.1.6 on 2025-02-28 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("assidu", "0002_task_interval_days_alter_task_user_accomplishment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="accomplishment",
            name="notes",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="task",
            name="enddate",
            field=models.DateField(blank=True, null=True),
        ),
    ]
