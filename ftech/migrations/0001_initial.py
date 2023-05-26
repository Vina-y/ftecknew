# Generated by Django 4.2.1 on 2023-05-21 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bookDemo',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('email', models.EmailField(error_messages={'unique': 'Email address already exists.'}, max_length=100, unique=True)),
                ('subject', models.TextField()),
                ('message', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'book_demo',
                'managed': True,
            },
        ),
    ]
