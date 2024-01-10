# Generated by Django 4.1.2 on 2024-01-10 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0009_product_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productcolor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=5, verbose_name='رنگ')),
                ('url_title', models.CharField(db_index=True, max_length=30, unique=True, verbose_name='نام در url')),
                ('is_active', models.BooleanField(verbose_name='فعال / غیرفعال')),
            ],
            options={
                'verbose_name': 'رنگ',
                'verbose_name_plural': 'رنگ ها',
            },
        ),
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.ManyToManyField(related_name='product_color', to='product_module.productcolor', verbose_name='رنگ'),
        ),
    ]