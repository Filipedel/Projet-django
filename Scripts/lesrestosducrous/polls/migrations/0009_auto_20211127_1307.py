# Generated by Django 3.2.9 on 2021-11-27 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_beneficiaire'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beneficiaire',
            name='remarque',
        ),
        migrations.RemoveField(
            model_name='beneficiaire',
            name='valide',
        ),
    ]
