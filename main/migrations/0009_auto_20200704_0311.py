# Generated by Django 3.0.7 on 2020-07-03 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20200704_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_posted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
