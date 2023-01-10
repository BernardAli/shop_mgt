# Generated by Django 4.1.4 on 2023-01-10 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_cash_cashhistory"),
    ]

    operations = [
        migrations.AddField(
            model_name="stock",
            name="yet_to_deliver",
            field=models.IntegerField(blank=True, default="0", null=True),
        ),
        migrations.AlterField(
            model_name="cash",
            name="category",
            field=models.CharField(
                blank=True,
                choices=[("Bank", "Bank"), ("Cash", "Cash"), ("Momo", "Momo")],
                max_length=50,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="cashhistory",
            name="category",
            field=models.CharField(
                blank=True,
                choices=[("Bank", "Bank"), ("Cash", "Cash"), ("Momo", "Momo")],
                max_length=50,
                null=True,
            ),
        ),
    ]
