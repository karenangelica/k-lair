# Generated by Django 3.0.7 on 2020-07-03 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200629_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='code_posted',
            field=models.TimeField(auto_now_add=True),
        ),
    ]