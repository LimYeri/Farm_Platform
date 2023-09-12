# Generated by Django 4.2.4 on 2023-08-17 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tran", "0036_alter_tran_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tran",
            name="type",
            field=models.CharField(
                choices=[
                    ("herbs", "나물"),
                    ("nuts", "견과류"),
                    ("root", "뿌리"),
                    ("vegetable", "채소"),
                    ("fruits", "과일"),
                    ("grain", "곡물"),
                    ("mushroom", "버섯"),
                    ("non-specified", "기타 작물"),
                ],
                max_length=400,
                null=True,
            ),
        ),
    ]
