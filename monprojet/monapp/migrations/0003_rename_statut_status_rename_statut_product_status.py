# Generated by Django 5.1.1 on 2024-09-10 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monapp', '0002_statut_product_date_de_fabrication_product_prix_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Statut',
            new_name='Status',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='statut',
            new_name='status',
        ),
    ]
