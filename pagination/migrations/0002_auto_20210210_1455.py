# Generated by Django 3.1.4 on 2021-02-10 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagination', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paginationdata',
            name='data_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='paginationdata',
            name='data_serial_number',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
