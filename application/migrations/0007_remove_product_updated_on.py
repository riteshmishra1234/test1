# Generated by Django 3.1.5 on 2021-01-29 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_remove_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='updated_on',
        ),
    ]