# Generated by Django 4.2.7 on 2023-12-06 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='İsim')),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=50, verbose_name='Konu')),
                ('message', models.TextField(max_length=255, verbose_name='Mesaj')),
                ('status', models.CharField(choices=[('New', 'Yeni'), ('Read', 'Okundu'), ('Closed', 'Kapandı')], default='New', max_length=10, verbose_name='Durum')),
                ('ip', models.GenericIPAddressField()),
                ('adminnote', models.CharField(blank=True, max_length=100, verbose_name='Not')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme')),
            ],
        ),
    ]
