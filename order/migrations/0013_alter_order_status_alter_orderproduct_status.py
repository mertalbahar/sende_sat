# Generated by Django 4.2.7 on 2023-12-05 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_alter_order_status_alter_orderproduct_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Yeni', 'Yeni'), ('İşleme Alındı', 'İşleme Alındı'), ('Tamamlandı', 'Tamamlandı'), ('İptal Edildi', 'İptal Edildi')], default='Yeni', max_length=15, verbose_name='Durum'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='status',
            field=models.CharField(choices=[('Yeni', 'Yeni'), ('İşleme Alındı', 'İşleme Alındı'), ('Hazırlanıyor', 'Hazırlanıyor'), ('Kargolandı', 'Kargolandı'), ('Tamamlandı', 'Tamamlandı'), ('İptal Edildi', 'İptal Edildi')], default='Yeni', max_length=15, verbose_name='Durum'),
        ),
    ]
