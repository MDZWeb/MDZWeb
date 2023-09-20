# Generated by Django 4.2.5 on 2023-09-12 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphicdesigns', '0002_rename_graphicdesign_graphic_designs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graphic_designs',
            name='design_type',
            field=models.CharField(choices=[('Social Media Design', 'Social Media Design'), ('Face Book Covers', 'Face Book Covers'), ('Flyer Design', 'Flyer Design'), ('Business Card Design', 'Business Card Design')], default='Social Media Design', max_length=300),
        ),
    ]
