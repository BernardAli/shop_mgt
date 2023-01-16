# Generated by Django 4.1.4 on 2023-01-11 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_stock_receipt_no_alter_stock_payment_status_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="stockhistory",
            name="receipt_no",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="stock",
            name="payment_status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Credit", "Credit"),
                    ("Full Payment", "Full Payment"),
                    ("Part Payment", "Part Payment"),
                    ("Take Balance", "Take Balance"),
                ],
                max_length=50,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="stockhistory",
            name="payment_status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Credit", "Credit"),
                    ("Full Payment", "Full Payment"),
                    ("Part Payment", "Part Payment"),
                    ("Take Balance", "Take Balance"),
                ],
                max_length=50,
                null=True,
            ),
        ),
    ]