# Generated by Django 4.2.7 on 2023-12-06 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contact'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='ContactMessage',
        ),
    ]
