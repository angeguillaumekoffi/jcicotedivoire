# Generated by Django 2.2 on 2019-08-22 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Presidents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonneesPresi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordre', models.CharField(choices=[('National', 'National'), ('International', 'international')], max_length=15, verbose_name='Ordre')),
                ('mdt', models.CharField(max_length=10, verbose_name='Mandat')),
                ('Nom_Pren', models.CharField(max_length=100, verbose_name='Nom et prenoms')),
                ('origin', models.CharField(max_length=40, verbose_name='Origine')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='Presidents/', verbose_name='Photo')),
            ],
            options={
                'db_table': 'DonneesPresident',
            },
        ),
    ]
