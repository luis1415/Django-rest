# Generated by Django 2.1.5 on 2019-01-06 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_gamersdb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamersdb',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
