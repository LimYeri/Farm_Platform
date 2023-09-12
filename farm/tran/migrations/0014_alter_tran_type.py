# Generated by Django 4.2.4 on 2023-08-16 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tran", "0013_alter_tran_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tran",
            name="type",
            field=models.CharField(
                choices=[
                    ("grain", "곡물"),
                    ("non-specified", "기타 작물"),
                    ("nuts", "견과류"),
                    ("fruits", "과일"),
                    ("mushroom", "버섯"),
                    ("root", "뿌리"),
                    ("herbs", "나물"),
                    ("vegetable", "채소"),
                ],
                max_length=400,
                null=True,
            ),
        ),
    ]
