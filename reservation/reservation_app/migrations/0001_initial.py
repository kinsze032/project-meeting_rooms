# Generated by Django 3.2.16 on 2023-02-08 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConferenceRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('capacity', models.PositiveIntegerField()),
                ('projector_availability', models.BooleanField(default=False)),
            ],
        ),
    ]
