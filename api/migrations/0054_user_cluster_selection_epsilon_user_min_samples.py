# Generated by Django 4.2.1 on 2023-07-11 11:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0053_user_confidence_unknown_face_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="cluster_selection_epsilon",
            field=models.FloatField(default=0.05),
        ),
        migrations.AddField(
            model_name="user",
            name="min_samples",
            field=models.IntegerField(default=1),
        ),
    ]