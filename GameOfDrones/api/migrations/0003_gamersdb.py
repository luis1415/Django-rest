# Generated by Django 2.1.5 on 2019-01-06 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_simplegame'),
    ]

    operations = [
        migrations.CreateModel(
            name='GamersDB',
            fields=[
                ('id', models.CharField(auto_created=True, max_length=10, primary_key=True, serialize=False)),
                ('player_1', models.CharField(max_length=32)),
                ('player_2', models.CharField(max_length=32)),
            ],
        ),
    ]