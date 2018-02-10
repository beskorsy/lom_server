# Generated by Django 2.0.2 on 2018-02-10 22:20

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20180210_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, unique=True)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, default=1, max_digits=5)),
            ],
        ),
        migrations.DeleteModel(
            name='Bucketlist',
        ),
    ]
