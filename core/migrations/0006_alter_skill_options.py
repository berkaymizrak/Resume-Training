# Generated by Django 4.1.5 on 2023-02-23 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_skill'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ('order',), 'verbose_name': 'Skill', 'verbose_name_plural': 'Skills'},
        ),
    ]
