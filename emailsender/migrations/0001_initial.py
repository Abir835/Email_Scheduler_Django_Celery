# Generated by Django 3.1.7 on 2022-04-23 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_email', models.CharField(blank=True, max_length=50, null=True)),
                ('to_email', models.CharField(blank=True, max_length=50, null=True)),
                ('subject', models.CharField(blank=True, max_length=50, null=True)),
                ('body', models.TextField(blank=True, max_length=499, null=True)),
                ('date', models.CharField(blank=True, max_length=50, null=True)),
                ('is_active', models.IntegerField(blank=True, default=0, null=True)),
                ('is_delete', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]