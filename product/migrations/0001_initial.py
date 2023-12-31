# Generated by Django 4.2.7 on 2023-11-26 14:14

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Kategori')),
                ('keywords', models.CharField(max_length=250)),
                ('description', models.TextField(verbose_name='Açıklama')),
                ('image', models.ImageField(blank=True, upload_to='images/category/', verbose_name='Resim')),
                ('status', models.CharField(choices=[('True', 'Evet'), ('False', 'Hayır')], default=False, max_length=10, verbose_name='Yayınla')),
                ('slug', models.SlugField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('mptt_level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='product.category')),
            ],
            options={
                'verbose_name': 'Kategori',
                'verbose_name_plural': 'Kategoriler',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Ürün')),
                ('keywords', models.CharField(max_length=250)),
                ('description', models.TextField(verbose_name='Açıklama')),
                ('image', models.ImageField(blank=True, upload_to='images/', verbose_name='Resim')),
                ('price', models.FloatField(verbose_name='Birim Fiyat')),
                ('quantity', models.IntegerField(default=0, verbose_name='Adet')),
                ('detail', models.TextField(verbose_name='Detay')),
                ('status', models.CharField(choices=[('True', 'Evet'), ('False', 'Hayır')], max_length=10, verbose_name='Yayınla')),
                ('slug', models.SlugField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
            options={
                'verbose_name': 'Ürün',
                'verbose_name_plural': 'Ürünler',
            },
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Başlık')),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'verbose_name': 'Resim',
                'verbose_name_plural': 'Resimler',
            },
        ),
    ]
