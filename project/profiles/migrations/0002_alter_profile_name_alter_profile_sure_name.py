# Generated by Django 4.2.2 on 2023-06-17 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Sure_Name',
            field=models.CharField(max_length=50),
        ),
    ]
