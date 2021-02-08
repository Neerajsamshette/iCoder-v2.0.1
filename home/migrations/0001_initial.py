# Generated by Django 3.1.6 on 2021-02-06 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=40)),
                ('email', models.CharField(default='', max_length=50)),
                ('phone_number', models.IntegerField(default='', max_length=10)),
                ('issue_message', models.CharField(default='', max_length=200)),
            ],
        ),
    ]