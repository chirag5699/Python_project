# Generated by Django 4.2.2 on 2023-07-14 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_seller', '0019_alter_listing_data_p_price_and_more'),
        ('app_bayur', '0008_remove_cart_bayer_id_remove_cart_product_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propic', models.FileField(default='anonymous.jpg', upload_to='media/')),
                ('firstname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('Mobile_No', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='checkout_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile_no', models.IntegerField(default=0)),
                ('address1', models.CharField(max_length=1000)),
                ('address2', models.CharField(max_length=1000)),
                ('City', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=50)),
                ('Country', models.CharField(max_length=50)),
                ('ZIPCode', models.IntegerField(default=0)),
                ('order_id', models.CharField(max_length=50)),
                ('bayer_detials', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_bayur.add_user')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quntity', models.IntegerField(default=0)),
                ('product_color', models.CharField(max_length=50)),
                ('product_size', models.CharField(max_length=50)),
                ('total', models.IntegerField(default=0)),
                ('Bayer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_bayur.add_user')),
                ('Product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_seller.listing_data')),
            ],
        ),
    ]
