# Generated by Django 4.2.5 on 2023-09-08 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GraphicDesign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design_name', models.CharField(max_length=300)),
                ('design_type', models.CharField(max_length=300)),
                ('is_feature', models.BooleanField(default=True)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='Images/Graphic Design')),
            ],
            options={
                'verbose_name': 'Graphic Design',
                'verbose_name_plural': 'Graphic Designs',
            },
        ),
    ]
