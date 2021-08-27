# Generated by Django 3.2.3 on 2021-08-21 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10, verbose_name='عنوان')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('author', models.CharField(max_length=100, verbose_name='نویسنده')),
                ('inventory', models.PositiveIntegerField(verbose_name='موجودی')),
                ('price', models.DecimalField(decimal_places=5, max_digits=20, verbose_name='قیمت')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'کتاب',
                'verbose_name_plural': 'کتاب ها',
            },
        ),
    ]