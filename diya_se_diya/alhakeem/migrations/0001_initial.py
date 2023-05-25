# Generated by Django 4.2.1 on 2023-05-24 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('firstName', models.CharField(help_text='Enter your first name', max_length=200)),
                ('lastName', models.CharField(help_text='Enter your last name', max_length=200)),
                ('email', models.CharField(help_text='Enter your email', max_length=200)),
                ('phone', models.CharField(help_text='Enter your phone', max_length=200)),
            ],
        ),
    ]
