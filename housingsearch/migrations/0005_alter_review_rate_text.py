# Generated by Django 3.2.7 on 2021-10-24 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housingsearch', '0004_auto_20211023_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rate_text',
            field=models.CharField(max_length=200),
        ),
    ]