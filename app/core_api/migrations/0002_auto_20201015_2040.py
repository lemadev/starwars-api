# Generated by Django 2.1.15 on 2020-10-15 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='height',
            new_name='id_personaje',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='mass',
            new_name='puntaje',
        ),
        migrations.RemoveField(
            model_name='character',
            name='average_rating',
        ),
        migrations.RemoveField(
            model_name='character',
            name='birth_year',
        ),
        migrations.RemoveField(
            model_name='character',
            name='eye_color',
        ),
        migrations.RemoveField(
            model_name='character',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='character',
            name='hair_color',
        ),
        migrations.RemoveField(
            model_name='character',
            name='homeworld',
        ),
        migrations.RemoveField(
            model_name='character',
            name='max_rating',
        ),
        migrations.RemoveField(
            model_name='character',
            name='name',
        ),
        migrations.RemoveField(
            model_name='character',
            name='skin_color',
        ),
        migrations.RemoveField(
            model_name='character',
            name='species',
        ),
    ]
