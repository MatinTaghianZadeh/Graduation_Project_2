# Generated by Django 5.0.3 on 2025-01-12 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_groupchat_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupchat',
            name='description',
            field=models.TextField(default='', max_length=255),
        ),
    ]
