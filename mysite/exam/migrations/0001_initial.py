# Generated by Django 4.0.4 on 2022-04-28 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ogretmen_adi', models.CharField(max_length=100)),
                ('ders_kodu', models.CharField(max_length=30, unique=True)),
                ('ders_adi', models.CharField(max_length=100)),
                ('birim_adi', models.CharField(blank=True, max_length=50, null=True)),
                ('ogrenci_sayisi', models.IntegerField(default=0)),
            ],
        ),
    ]
