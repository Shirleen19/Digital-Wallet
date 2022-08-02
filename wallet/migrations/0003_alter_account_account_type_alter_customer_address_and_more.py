# Generated by Django 4.0.6 on 2022-08-02 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0002_account_currency_receipt_customer_profile_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_type',
            field=models.CharField(choices=[('P', 'Personal Account'), ('B', 'Business Account')], max_length=20),
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=95),
        ),
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('NB', 'Non-Binary')], max_length=10),
        ),
    ]
