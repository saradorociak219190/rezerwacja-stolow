# Generated by Django 2.0.3 on 2018-03-15 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReservationElements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservations_text', models.CharField(max_length=200)),
                ('done', models.BooleanField()),
            ],
        ),
    ]
