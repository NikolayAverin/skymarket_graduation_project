# Generated by Django 3.2.6 on 2024-08-27 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_user_role"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                blank=True,
                choices=[("admin", "Администратор"), ("user", "Пользователь")],
                max_length=10,
                null=True,
                verbose_name="Роль",
            ),
        ),
    ]
