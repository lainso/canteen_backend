# Generated by Django 4.1.7 on 2023-11-24 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0002_rename_ord_customer_order_cus_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="employee",
            old_name="emp_conditon",
            new_name="emp_condition",
        ),
    ]
