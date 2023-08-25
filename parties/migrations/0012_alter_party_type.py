# Generated by Django 4.2.2 on 2023-08-24 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parties', '0011_member_slipimage_party_promptpay_party_timecreate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='type',
            field=models.CharField(choices=[('F', 'Food&Drink'), ('H', 'Home&Hotel'), ('S', 'Subscribe&Service')], max_length=1),
        ),
    ]