# Generated by Django 4.2.2 on 2023-07-12 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parties', '0004_member_party'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='party',
            name='host',
        ),
        migrations.AlterField(
            model_name='member',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
        migrations.AlterField(
            model_name='party',
            name='menu',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='party',
            name='partyName',
            field=models.CharField(max_length=30),
        ),
    ]
