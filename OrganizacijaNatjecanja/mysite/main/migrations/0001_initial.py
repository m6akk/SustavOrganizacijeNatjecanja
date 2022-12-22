# Generated by Django 4.1.4 on 2022-12-22 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Natjecaj',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('natjecaj_naziv', models.CharField(max_length=50)),
                ('natjecaj_broj', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Natjecatelj',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('natjecatelj_ime', models.CharField(max_length=25)),
                ('natjecatelj_prezime', models.CharField(max_length=25)),
                ('natjecatelj_OIB', models.IntegerField()),
                ('natjecatelj_natjecaji', models.ManyToManyField(to='main.natjecaj')),
            ],
        ),
        migrations.CreateModel(
            name='Organizator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organizator_naziv', models.CharField(max_length=50)),
                ('organizator_OIB', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Kontakt',
            fields=[
                ('kontakt_natjecatelj_email', models.CharField(max_length=50)),
                ('kontakt_natjecatelj_mobitel', models.CharField(max_length=50)),
                ('kontakt_natjecatelj', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.natjecatelj')),
            ],
        ),
        migrations.AddField(
            model_name='natjecaj',
            name='natjecaj_organizator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.organizator'),
        ),
    ]