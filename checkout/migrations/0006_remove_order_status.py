# Generated by Django 3.2.9 on 2024-07-12 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
    ]
