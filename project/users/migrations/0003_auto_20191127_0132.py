# Generated by Django 2.2.7 on 2019-11-27 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='perfil',
            field=models.CharField(choices=[(1, 'candidato'), (2, 'empresa')], max_length=200),
        ),
    ]
