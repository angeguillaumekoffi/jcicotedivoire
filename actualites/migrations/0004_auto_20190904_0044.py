# Generated by Django 2.2 on 2019-09-04 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actualites', '0003_auto_20190904_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='cont_msg',
            field=models.TextField(verbose_name='Message'),
        ),
    ]
