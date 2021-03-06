# Generated by Django 3.0.3 on 2020-02-17 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aviata', '0002_auto_20200217_1314'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_token', models.TextField()),
                ('price', models.FloatField()),
                ('time', models.DateTimeField()),
                ('airline', models.CharField(max_length=255)),
                ('duration', models.CharField(max_length=255)),
                ('seats', models.IntegerField()),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aviata.Route')),
            ],
        ),
    ]
