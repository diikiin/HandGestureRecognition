# Generated by Django 4.1 on 2022-11-26 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hand_gesture", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="handgesture",
            name="translation_key",
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="translation",
            name="key",
            field=models.CharField(db_index=True, max_length=255),
        ),
    ]
