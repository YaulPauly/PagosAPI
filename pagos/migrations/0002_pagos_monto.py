# Generated by Django 4.1.4 on 2022-12-16 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagos',
            name='monto',
            field=models.FloatField(default=0.0),
        ),
    ]
