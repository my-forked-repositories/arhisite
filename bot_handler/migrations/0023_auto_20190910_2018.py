# Generated by Django 2.2.4 on 2019-09-10 16:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('bot_handler', '0022_auto_20190910_1948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='item',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='user',
        ),
        migrations.RemoveField(
            model_name='user',
            name='seller',
        ),
        migrations.RemoveField(
            model_name='user',
            name='sex',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='Purchase',
        ),
        migrations.DeleteModel(
            name='Seller',
        ),
    ]
