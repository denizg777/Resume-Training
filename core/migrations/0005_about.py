# Generated by Django 5.0.4 on 2024-05-18 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_work'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', help_text='This is variable of the setting.', max_length=254, verbose_name='Name')),
                ('description', models.CharField(blank=True, default='', max_length=254, verbose_name='Description')),
                ('parameter', models.CharField(blank=True, default='', max_length=254, verbose_name='Parameter')),
                ('updated_date', models.DateField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Created Date')),
            ],
            options={
                'verbose_name': 'About',
                'ordering': ('name',),
            },
        ),
    ]