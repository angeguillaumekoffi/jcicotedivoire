# Generated by Django 2.2 on 2019-09-04 01:05

import ckeditor.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20190808_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formation',
            name='adherant',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile', verbose_name='Adherant'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Datn',
            field=models.DateField(blank=True, null=True, verbose_name='Date de naissance'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Sit_matri',
            field=models.CharField(blank=True, choices=[('EN COUPLE', 'en couple'), ('CELLIBATAIRE', 'cellibataire'), ('DIVORCE(E)', 'divorcé(e)')], default='Cellibataire', max_length=13, verbose_name='Situation matrimoniale'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='actv_inter',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Activites internationales'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='actv_loc',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Activites locales'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='actv_nat',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Activites nationales'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='actv_zon',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Activites zonales'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bp',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Boite postale'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='commiss',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='commission'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='conjoint',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Conjoint(e)'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='dat_pc',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 9, 4, 1, 5, 18, 752890, tzinfo=utc), null=True, verbose_name='Date de Prise de contact'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='employ',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Employeur'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nom_pren',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Nom et Prenoms'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='olm',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='OLM.OLM', verbose_name='OLM'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='par_mar',
            field=models.CharField(blank=True, max_length=50, verbose_name='Parrain/marraine'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='prof',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Profession'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='tel',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Tel/Cel'),
        ),
        migrations.AlterField(
            model_name='publications',
            name='pub_par',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile', verbose_name='auteur'),
        ),
        migrations.AlterField(
            model_name='publications',
            name='pub_text',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Contenu'),
        ),
    ]
