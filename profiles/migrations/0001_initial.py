# Generated by Django 2.2 on 2019-08-08 18:03

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import profiles.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authtools', '0003_auto_20160128_0912'),
        ('OLM', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('slug', models.UUIDField(blank=True, default=uuid.uuid4, editable=False)),
                ('picture', models.ImageField(blank=True, null=True, upload_to=profiles.models.phot_profile, verbose_name='Photo de Profile')),
                ('email_verified', models.BooleanField(default=False, verbose_name='Email verifié')),
                ('nom_pren', models.CharField(default='', max_length=100, verbose_name='Nom et Prenoms')),
                ('Datn', models.DateField(blank=True, verbose_name='Date de naissance')),
                ('Sit_matri', models.CharField(choices=[('EN COUPLE', 'en couple'), ('CELLIBATAIRE', 'cellibataire'), ('DIVORCE(E)', 'divorcé(e)')], default='Cellibataire', max_length=13, verbose_name='Situation matrimoniale')),
                ('conjoint', models.CharField(max_length=100, null=True, verbose_name='Conjoint(e)')),
                ('prof', models.CharField(max_length=20, null=True, verbose_name='Profession')),
                ('employ', models.CharField(max_length=50, null=True, verbose_name='Employeur')),
                ('tel', models.CharField(max_length=30, verbose_name='Tel/Cel')),
                ('bp', models.CharField(max_length=20, null=True, verbose_name='Boite postale')),
                ('dat_pc', models.DateField(blank=True, default=datetime.datetime(2019, 8, 8, 18, 2, 59, 127793), verbose_name='Date de Prise de contact')),
                ('commiss', models.PositiveIntegerField(null=True, verbose_name='commission')),
                ('par_mar', models.CharField(max_length=50, verbose_name='Parrain/marraine')),
                ('actv_loc', models.CharField(max_length=300, null=True, verbose_name='Activites locales')),
                ('actv_zon', models.CharField(max_length=300, null=True, verbose_name='Activites zonales')),
                ('actv_nat', models.CharField(max_length=300, null=True, verbose_name='Activites nationales')),
                ('actv_inter', models.CharField(max_length=200, null=True, verbose_name='Activites internationales')),
                ('bio', models.CharField(blank=True, max_length=200, null=True, verbose_name='Bio')),
                ('olm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OLM.OLM', verbose_name='OLM')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Publications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_dat', models.DateTimeField(auto_now=True, verbose_name='Publié le')),
                ('pub_text', models.TextField(blank=True, null=True, verbose_name='Contenu')),
                ('pub_file', models.FileField(blank=True, null=True, upload_to=profiles.models.publication, verbose_name='Image, vidéo')),
                ('pub_like', models.IntegerField(blank=True, null=True, verbose_name='Likes')),
                ('pub_par', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile', verbose_name='auteur')),
            ],
        ),
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=100, null=True, verbose_name='Theme')),
                ('forma_dat', models.DateField(null=True, verbose_name='Dates')),
                ('formateur', models.CharField(max_length=100, null=True, verbose_name='Formateurs')),
                ('adherant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile', verbose_name='Adherant')),
            ],
            options={
                'db_table': 'Formations',
            },
        ),
    ]