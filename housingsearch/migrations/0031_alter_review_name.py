# Generated by Django 3.2.7 on 2021-11-28 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housingsearch', '0030_alter_review_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='name',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
