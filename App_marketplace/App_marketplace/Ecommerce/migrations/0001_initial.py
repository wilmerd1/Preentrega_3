# Generated by Django 5.0.4 on 2024-05-02 01:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoriaproducto',
            fields=[
                ('categoria_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('tipo', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cliente_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('direccion', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'cliente',
                'verbose_name_plural': 'clientes',
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('delivery_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('tipo', models.CharField(max_length=200)),
                ('estatus', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'delivery',
                'verbose_name_plural': 'deliveries',
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('pedido_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('date', models.DateTimeField()),
                ('status', models.CharField(max_length=200)),
                ('cliente_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ecommerce.cliente')),
                ('delivery_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ecommerce.delivery')),
            ],
            options={
                'verbose_name': 'pedido',
                'verbose_name_plural': 'pedidos',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('producto_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descripcion', models.TextField()),
                ('categoria_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ecommerce.categoriaproducto')),
            ],
            options={
                'verbose_name': 'producto',
                'verbose_name_plural': 'productos',
            },
        ),
    ]
