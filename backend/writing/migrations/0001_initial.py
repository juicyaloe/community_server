# Generated by Django 4.1 on 2022-08-29 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Writing",
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
                ("title", models.CharField(max_length=200)),
                ("content", models.TextField()),
                ("inittime", models.DateTimeField(auto_now=True)),
                (
                    "board",
                    models.CharField(
                        choices=[("airplane", "Airplane"), ("car", "Car")],
                        default="airplane",
                        max_length=10,
                    ),
                ),
            ],
        ),
    ]
