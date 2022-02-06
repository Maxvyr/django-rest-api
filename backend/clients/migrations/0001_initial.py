# Generated by Django 4.0.2 on 2022-02-06 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=500)),
                ('age', models.FloatField(default=0)),
                ('sexe', models.IntegerField(default=0)),
            ],
        ),
    ]
