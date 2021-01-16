# Generated by Django 2.2.2 on 2021-01-05 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_auto_20210105_1953'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParticipantRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=12)),
                ('emailID', models.EmailField(max_length=254)),
                ('eventList', models.DateTimeField()),
                ('registrationType', models.CharField(max_length=255)),
                ('noOfPeople', models.IntegerField()),
            ],
        ),
    ]