# Generated by Django 4.1.7 on 2023-03-07 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("application", "0004_alter_income_user_alter_non_creamy_layer_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="role",
            field=models.CharField(default="user", max_length=10),
        ),
    ]