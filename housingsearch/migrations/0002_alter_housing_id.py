# Generated by Django 3.2.7 on 2021-10-24 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housingsearch', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housing',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]