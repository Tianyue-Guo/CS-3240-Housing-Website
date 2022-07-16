# Generated by Django 3.2.7 on 2021-10-29 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('housingsearch', '0008_review_review_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate_text', models.CharField(max_length=200)),
                ('rate', models.IntegerField(default=0)),
                ('housing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='housingsearch.housing')),
            ],
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]