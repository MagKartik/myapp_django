# Generated by Django 4.2 on 2023-04-26 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('recipe', models.TextField()),
                ('recipe_name', models.CharField(max_length=255)),
            ],
        ),
    ]