# Generated by Django 2.2 on 2019-09-04 00:27

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Activites', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activites',
            name='contenu_actv',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Contenu'),
        ),
    ]
