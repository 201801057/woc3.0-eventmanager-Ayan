# Generated by Django 2.2.2 on 2021-01-23 17:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0006_auto_20210123_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventregistration',
            name='password',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
