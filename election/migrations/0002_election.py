# Generated by Django 2.1 on 2018-09-07 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Election',
            fields=[
                ('election_id', models.AutoField(primary_key=True, serialize=False)),
                ('election_name', models.CharField(max_length=50)),
                ('election_date', models.DateField(null=True)),
                ('candidate_count', models.IntegerField(default=0)),
            ],
        ),
    ]
