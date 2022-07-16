# Generated by Django 3.2.7 on 2021-11-12 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housingsearch', '0018_alter_housing_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='End_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=300, null=True)),
                ('city', models.CharField(max_length=300, null=True)),
                ('state', models.CharField(max_length=300, null=True)),
                ('zip', models.CharField(max_length=5, null=True)),
                ('phone_number', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
