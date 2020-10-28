# Generated by Django 3.1.2 on 2020-10-01 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, verbose_name='VCA2142')),
                ('description', models.CharField(max_length=255, verbose_name='20% off all products')),
                ('discount', models.FloatField(verbose_name=0.2)),
            ],
        ),
    ]
