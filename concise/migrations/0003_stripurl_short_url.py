# Generated by Django 3.1 on 2020-11-09 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concise', '0002_remove_stripurl_short_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='stripurl',
            name='short_url',
            field=models.URLField(null=True),
        ),
    ]
