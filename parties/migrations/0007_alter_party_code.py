# Generated by Django 4.2.2 on 2023-07-13 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parties', '0006_party_host'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='Code',
            field=models.CharField(default='', max_length=5, unique=True),
        ),
    ]
