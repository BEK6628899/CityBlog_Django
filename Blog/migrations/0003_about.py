# Generated by Django 4.2 on 2023-05-01 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_din_vaqt_alter_din_din_malumot_alter_din_rasm_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasm', models.FileField(upload_to='')),
            ],
        ),
    ]
