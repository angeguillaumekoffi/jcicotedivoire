# Generated by Django 2.2 on 2019-08-08 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BandeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dat_pub', models.DateTimeField(auto_now=True, verbose_name='Date de publication')),
                ('info', models.CharField(max_length=200, null=True, verbose_name='Info')),
            ],
            options={
                'db_table': "Bande d'info",
            },
        ),
        migrations.CreateModel(
            name='Statut_Activite',
            fields=[
                ('statut', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='Statut')),
            ],
        ),
        migrations.CreateModel(
            name='Activites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100, null=True, verbose_name='Titre')),
                ('date_pub', models.DateTimeField(auto_now=True, verbose_name='Date de publication')),
                ('contenu_actv', models.TextField(null=True, verbose_name='Contenu')),
                ('img', models.ImageField(null=True, upload_to='images/')),
                ('statut_actv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Activites.Statut_Activite', verbose_name='Statut')),
            ],
            options={
                'db_table': 'Activites',
            },
        ),
    ]