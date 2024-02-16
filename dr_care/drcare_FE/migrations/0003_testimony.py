# Generated by Django 5.0.1 on 2024-02-04 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drcare_FE', '0002_alter_contactus_email_alter_contactus_phonecontact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimony',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, max_length=50)),
                ('occupation', models.CharField(blank=True, max_length=50)),
                ('testimony', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Testimony',
                'verbose_name_plural': 'Testimonys',
            },
        ),
    ]
