# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sites',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('site_name', models.CharField(max_length=10)),
                ('Date', models.DateField()),
                ('Avalue', models.FloatField()),
                ('Bvalue', models.FloatField()),
            ],
        ),
    ]
