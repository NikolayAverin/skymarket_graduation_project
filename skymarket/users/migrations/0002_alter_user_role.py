# Generated by Django 3.2.6 on 2024-08-20 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[("admin", "Администратор"), ("user", "Пользователь")],
                default="user",
                max_length=10,
                verbose_name="Роль",
            ),
        ),
    ]
