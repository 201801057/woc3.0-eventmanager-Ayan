# Generated by Django 2.2.2 on 2021-01-23 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0007_eventregistration_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventregistration',
            name='eventId',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='participantregistration',
            name='pId',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
