# Generated by Django 2.0.7 on 2018-07-28 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0002_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='category',
            field=models.CharField(default='', max_length=120),
        ),
    ]
