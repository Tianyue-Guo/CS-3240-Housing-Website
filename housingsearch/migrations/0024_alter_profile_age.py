# Generated by Django 3.2.7 on 2021-11-13 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housingsearch', '0023_auto_20211113_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.CharField(default=' ', max_length=3, null=True),
        ),
    ]
