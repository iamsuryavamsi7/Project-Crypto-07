# Generated by Django 4.2.7 on 2023-11-01 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='Destination_Pics')),
            ],
        ),
    ]