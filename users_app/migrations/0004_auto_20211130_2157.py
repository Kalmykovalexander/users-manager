# Generated by Django 3.2.9 on 2021-11-30 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0003_alter_usersgroups_index_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='groups',
            options={'verbose_name': 'group', 'verbose_name_plural': 'groups'},
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]
