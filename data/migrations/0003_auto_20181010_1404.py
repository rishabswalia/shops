# Generated by Django 2.0.6 on 2018-10-10 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20181010_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='productlink',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(max_length=20, null=True),
        ),
    ]