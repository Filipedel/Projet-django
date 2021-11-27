# Generated by Django 3.2.9 on 2021-11-27 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_delete_beneficiaire2'),
    ]

    operations = [
        migrations.CreateModel(
            name='beneficiaire2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=10)),
                ('adresse', models.EmailField(max_length=254)),
                ('nbParts', models.IntegerField()),
                ('motMairie', models.BooleanField()),
                ('carteDonnee', models.BooleanField()),
                ('presenceDistribution', models.DateField()),
                ('valide', models.BooleanField()),
            ],
        ),
    ]
