# Generated by Django 3.1.2 on 2020-10-31 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0002_worker_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='ended_at',
            field=models.DateTimeField(db_index=True, null=True),
        ),
    ]