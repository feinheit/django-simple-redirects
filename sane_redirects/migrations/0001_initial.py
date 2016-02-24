# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Redirect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('old_path', models.CharField(verbose_name='redirect from', max_length=200, help_text="This should be an absolute path, excluding the domain name. Example: '/events/search/'.", unique=True)),
                ('new_path', models.CharField(blank=True, verbose_name='redirect to', max_length=200, help_text="This can be either an absolute path (as above) or a full URL starting with 'http://'.")),
            ],
            options={
                'verbose_name_plural': 'redirects',
                'verbose_name': 'redirect',
                'ordering': ('old_path',),
            },
        ),
    ]
