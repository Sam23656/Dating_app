# Generated by Django 4.2.2 on 2023-06-14 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Sure_Name', models.CharField(max_length=30)),
                ('Age', models.PositiveIntegerField()),
                ('Status', models.CharField(choices=[('st', 'Учусь'), ('wk', 'Работаю'), ('sd', 'Туплю'), ('mm', 'Мамкин миллиардер'), ('mp', 'Мамин бродяга, папин симпотяга')], max_length=50)),
                ('Salary', models.IntegerField()),
                ('Description', models.TextField()),
            ],
        ),
    ]
