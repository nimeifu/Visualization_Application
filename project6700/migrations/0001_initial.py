# Generated by Django 5.0.7 on 2024-08-09 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Karaoke',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partyID', models.IntegerField()),
                ('NumberPeople', models.IntegerField()),
                ('Hours', models.IntegerField()),
                ('Session_Start_Time', models.IntegerField()),
                ('locationID', models.CharField(max_length=100)),
                ('Day_of_Week', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrderID', models.CharField(max_length=100)),
                ('Cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('TimePlaced', models.DateTimeField()),
                ('TimeDelivered', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RestaurantID', models.CharField(max_length=255)),
                ('Address', models.CharField(max_length=255)),
                ('Phone_number', models.CharField(max_length=255)),
                ('Owner_name', models.CharField(max_length=255)),
                ('Open_hours', models.CharField(max_length=255)),
            ],
        ),
    ]
