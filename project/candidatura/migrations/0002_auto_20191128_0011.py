# Generated by Django 2.2.7 on 2019-11-28 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('candidatura', '0001_initial'),
        ('vaga', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidatura',
            name='vaga',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vaga.Vaga'),
        ),
        migrations.AlterUniqueTogether(
            name='candidatura',
            unique_together={('vaga', 'candidato')},
        ),
    ]
