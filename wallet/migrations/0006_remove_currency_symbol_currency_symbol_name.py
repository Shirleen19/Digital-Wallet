# Generated by Django 4.0.6 on 2022-08-02 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0005_alter_currency_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currency',
            name='symbol',
        ),
        migrations.AddField(
            model_name='currency',
            name='symbol_name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
