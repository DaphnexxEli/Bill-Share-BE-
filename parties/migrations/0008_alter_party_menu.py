# Generated by Django 4.2.2 on 2023-07-25 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parties', '0007_alter_party_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='menu',
            field=models.CharField(default='', max_length=30),
        ),
    ]