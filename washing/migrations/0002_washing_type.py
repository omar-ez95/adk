# Generated by Django 3.2.3 on 2022-05-02 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('washing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='washing',
            name='type',
            field=models.IntegerField(choices=[(1, 'dryer'), (2, 'washing')], default=1),
        ),
    ]
