# Generated by Django 2.2.17 on 2021-01-10 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_auto_20210109_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comicinput',
            name='Type',
            field=models.CharField(choices=[('Reg', 'Reg'), ('Ann', 'Ann'), ('Spc', 'Spc')], default='Reg', max_length=30),
        ),
    ]
