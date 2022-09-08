# Generated by Django 4.1.1 on 2022-09-08 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("email", models.EmailField(max_length=120)),
                ("psword", models.CharField(max_length=100)),
                ("name", models.CharField(max_length=50)),
                ("address", models.CharField(max_length=120)),
            ],
            options={
                "db_table": "users",
            },
        ),
    ]