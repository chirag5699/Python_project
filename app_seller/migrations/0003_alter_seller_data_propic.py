# Generated by Django 4.2.2 on 2023-07-01 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_seller', '0002_alter_seller_data_propic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller_data',
            name='propic',
            field=models.FileField(default='anonymous.jpg', upload_to='seller/'),
        ),
    ]
