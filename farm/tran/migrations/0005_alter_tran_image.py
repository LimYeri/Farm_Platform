# Generated by Django 4.2.4 on 2023-08-13 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tran", "0004_alter_tran_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tran",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]
