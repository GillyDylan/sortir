# Generated by Django 2.1.3 on 2019-06-25 15:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Etat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Lieu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, unique=True)),
                ('rue', models.CharField(max_length=100, unique=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pseudo', models.CharField(max_length=50, unique=True)),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{10}$')])),
                ('administrateur', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sortie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('dateHeureDebut', models.DateTimeField()),
                ('dateHeureFin', models.DateTimeField()),
                ('dateLimiteInscription', models.DateField()),
                ('nbinscriptionMax', models.PositiveSmallIntegerField()),
                ('infosSortie', models.TextField()),
                ('etat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='SortirCom.Etat')),
                ('lieu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='SortirCom.Lieu')),
                ('organisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SortirCom.Participant')),
                ('participants', models.ManyToManyField(blank=True, related_name='sorties', to='SortirCom.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='Ville',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, unique=True)),
                ('codePostal', models.CharField(max_length=5, validators=[django.core.validators.RegexValidator('^\\d{5}$')])),
            ],
        ),
        migrations.AddField(
            model_name='participant',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='SortirCom.Site'),
        ),
        migrations.AddField(
            model_name='lieu',
            name='ville',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SortirCom.Ville'),
        ),
    ]
