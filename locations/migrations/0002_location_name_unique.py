# Generated by Django 3.0.7 on 2020-08-10 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
