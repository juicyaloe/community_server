# Generated by Django 4.1 on 2022-09-03 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("writing", "0003_delete_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="writing",
            name="writer",
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
