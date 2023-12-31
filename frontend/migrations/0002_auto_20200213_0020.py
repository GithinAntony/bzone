# Generated by Django 3.0.2 on 2020-02-12 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accommodation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('accommodation_name', models.CharField(max_length=100, null=True)),
                ('accommodation_address', models.TextField(max_length=100, null=True)),
                ('incharge_name', models.CharField(max_length=100, null=True)),
                ('person_to_contact', models.CharField(max_length=100, null=True)),
                ('committee_member', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Accomodated_candidates',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('accommodation_id', models.IntegerField(null=True)),
                ('candidate_id', models.IntegerField(null=True)),
                ('committee_member', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Candidates',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True)),
                ('institution_name', models.CharField(max_length=255, null=True)),
                ('email', models.CharField(max_length=255, null=True)),
                ('username', models.CharField(max_length=25, null=True)),
                ('password', models.CharField(max_length=255, null=True)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('address', models.TextField(null=True)),
                ('status', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CommitteeMembers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=255, null=True)),
                ('username', models.CharField(max_length=25, null=True)),
                ('password', models.CharField(max_length=255, null=True)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('address', models.TextField(null=True)),
                ('status', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('institution_name', models.CharField(max_length=100, null=True)),
                ('institution_address', models.TextField(max_length=100, null=True)),
                ('incharge_name', models.CharField(max_length=100, null=True)),
                ('person_to_contact', models.CharField(max_length=100, null=True)),
                ('committee_member', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Judges',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=255, null=True)),
                ('username', models.CharField(max_length=25, null=True)),
                ('password', models.CharField(max_length=255, null=True)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('address', models.TextField(null=True)),
                ('status', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Programs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('program_name', models.CharField(max_length=255, null=True)),
                ('committee_member', models.IntegerField(null=True)),
                ('details', models.TextField(null=True)),
                ('date', models.CharField(max_length=10, null=True)),
                ('time', models.CharField(max_length=25, null=True)),
                ('venue', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('program_id', models.IntegerField(null=True)),
                ('candidate_won', models.IntegerField(null=True)),
                ('candidate_grade', models.CharField(max_length=10, null=True)),
                ('judges_participated', models.IntegerField(null=True)),
                ('venue', models.CharField(max_length=100, null=True)),
                ('remarks', models.TextField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Locality',
        ),
        migrations.DeleteModel(
            name='Place',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
