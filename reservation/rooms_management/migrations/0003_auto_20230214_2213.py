# Generated by Django 3.2.16 on 2023-02-14 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms_management', '0002_roomreservation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roomreservation',
            old_name='room_id',
            new_name='room',
        ),
        migrations.AlterUniqueTogether(
            name='roomreservation',
            unique_together={('room', 'date')},
        ),
    ]
