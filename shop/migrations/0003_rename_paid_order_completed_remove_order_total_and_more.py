# Generated by Django 4.1.13 on 2024-05-19 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_orderitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='paid',
            new_name='completed',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='price',
        ),
    ]