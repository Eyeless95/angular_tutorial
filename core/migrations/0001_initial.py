# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 09:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('credit_card', models.IntegerField()),
                ('pin_code', models.IntegerField()),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_detail', models.CharField(max_length=128)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Account')),
            ],
        ),
    ]
