# Generated by Django 2.2 on 2019-09-04 00:27

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actualites', '0002_abonnes_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actualites',
            name='actu_descri',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='cont_msg',
            field=ckeditor.fields.RichTextField(verbose_name='Message'),
        ),
    ]
