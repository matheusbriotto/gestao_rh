# Generated by Django 3.0.4 on 2020-03-19 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0003_auto_20200319_0924'),
        ('funcionarios', '0004_auto_20200319_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='departamentos',
            field=models.ManyToManyField(to='departamentos.Departamento'),
        ),
    ]
