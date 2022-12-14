# Generated by Django 2.2 on 2022-10-20 13:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_garage_garagetool'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=50, verbose_name='Отчество')),
                ('date_of_birth', models.DateField(default=datetime.date.today, null=True, verbose_name='Дата рождения')),
                ('gender', models.SmallIntegerField(choices=[(0, 'Женский'), (1, 'Мужской')], default=1, verbose_name='Пол')),
            ],
            options={
                'verbose_name': 'Физическое лицо',
                'verbose_name_plural': 'Физические лица',
            },
        ),
        migrations.CreateModel(
            name='GarageStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('garage', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.Garage', verbose_name='Гараж')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.Person', verbose_name='Физ.лицо')),
            ],
            options={
                'verbose_name': 'Сотрудник гаража',
                'verbose_name_plural': 'Сотрудники гаража',
            },
        ),
    ]
