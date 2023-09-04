# Generated by Django 4.2 on 2023-05-05 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('eventDate', models.DateField()),
                ('eventData', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='users',
            name='id',
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False),
        ),
    ]
