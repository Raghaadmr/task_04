# Generated by Django 2.2.13 on 2020-08-30 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('opening_time', models.DateTimeField(auto_now_add=True)),
                ('closing_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]