# Generated by Django 4.2.2 on 2023-07-03 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parties', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='party',
            old_name='name',
            new_name='partyName',
        ),
    ]
