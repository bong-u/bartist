# Generated by Django 3.2.11 on 2022-01-07 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('value', models.IntegerField(primary_key=True, serialize=False)),
                ('recent', models.IntegerField()),
                ('image', models.URLField()),
            ],
        ),
    ]
