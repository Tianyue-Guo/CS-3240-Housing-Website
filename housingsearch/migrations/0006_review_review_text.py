# Generated by Django 3.2.7 on 2021-10-25 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housingsearch', '0005_alter_review_rate_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='review_text',
            field=models.CharField(default='', max_length=300),
        ),
    ]
