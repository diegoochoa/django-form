# Generated by Django 3.1.5 on 2021-01-14 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='direccion',
            field=models.CharField(default='null', max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]
