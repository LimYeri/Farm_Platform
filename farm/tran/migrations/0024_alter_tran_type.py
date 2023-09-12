# Generated by Django 4.2.4 on 2023-08-16 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tran", "0023_remove_tran_like_count_tran_like_user_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tran",
            name="type",
            field=models.CharField(
                choices=[
                    ("fruits", "과일"),
                    ("grain", "곡물"),
                    ("nuts", "견과류"),
                    ("root", "뿌리"),
                    ("vegetable", "채소"),
                    ("non-specified", "기타 작물"),
                    ("herbs", "나물"),
                    ("mushroom", "버섯"),
                ],
                max_length=400,
                null=True,
            ),
        ),
    ]
