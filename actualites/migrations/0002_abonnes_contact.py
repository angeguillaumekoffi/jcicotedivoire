# Generated by Django 2.2 on 2019-08-11 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actualites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abonnes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Abn_mail', models.EmailField(max_length=254, verbose_name='Email')),
                ('Abn_dat', models.DateTimeField(auto_now=True, verbose_name="Date d'envoi")),
            ],
            options={
                'db_table': 'Abonnés',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cont_nom', models.CharField(max_length=40, verbose_name='Nom')),
                ('cont_mail', models.EmailField(max_length=254, verbose_name='Email')),
                ('cont_obj', models.CharField(max_length=250, verbose_name='Objet')),
                ('cont_msg', models.TextField(verbose_name='Message')),
                ('cont_dat', models.DateTimeField(auto_now=True, verbose_name="Date d'envoi")),
            ],
            options={
                'db_table': 'Contacts',
            },
        ),
    ]