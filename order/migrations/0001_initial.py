# Generated by Django 4.2.5 on 2023-09-12 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=300)),
                ('last_name', models.CharField(max_length=300)),
                ('user_name', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=600)),
                ('contact', models.CharField(max_length=500)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('service', models.CharField(max_length=500)),
                ('order_status', models.CharField(choices=[('Active', 'Active'), ('Delivered', 'Delivered'), ('Revision', 'Revision'), ('Completed', 'Completed')], max_length=300)),
                ('order_details', models.TextField()),
            ],
        ),
    ]
