# Generated by Django 4.2.1 on 2023-06-03 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_remove_productinfo_external_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Контакты пользователя', 'verbose_name_plural': 'Контакты пользователя'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-dt',), 'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказ'},
        ),
        migrations.RemoveConstraint(
            model_name='productinfo',
            name='unique_product_info',
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='product',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_info', to='products.product', verbose_name='Продукт'),
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='shop',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_info', to='products.shop', verbose_name='Магазин'),
        ),
        migrations.AddConstraint(
            model_name='productinfo',
            constraint=models.UniqueConstraint(fields=('product', 'shop'), name='product_info'),
        ),
    ]
