# Generated by Django 4.2.7 on 2023-12-05 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_order_address_alter_order_city_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'Sepet', 'verbose_name_plural': 'Sepetler'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Sipariş', 'verbose_name_plural': 'Siparişler'},
        ),
        migrations.AlterModelOptions(
            name='orderproduct',
            options={'verbose_name': 'Sipariş Ürün', 'verbose_name_plural': 'Sipariş Ürünler'},
        ),
    ]