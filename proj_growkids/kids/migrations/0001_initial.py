# Generated by Django 2.2 on 2022-10-10 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='enroll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
                ('trainer_name', models.CharField(max_length=200)),
                ('studentname', models.CharField(max_length=200)),
                ('studentemail', models.CharField(max_length=200)),
                ('enrolldate', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='payment_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailid', models.CharField(max_length=200)),
                ('paidby', models.CharField(max_length=200)),
                ('amount', models.CharField(max_length=200)),
                ('paydate', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='trainer_reg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('qualification', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phoneno', models.CharField(max_length=20)),
                ('yearofexp', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='training_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
                ('trainer_name', models.CharField(max_length=200)),
                ('email_id', models.CharField(max_length=200)),
                ('details', models.CharField(max_length=200)),
                ('video', models.FileField(upload_to='video/')),
            ],
        ),
        migrations.CreateModel(
            name='UserLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=50)),
                ('utype', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='userprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastnaem', models.CharField(max_length=200)),
                ('dob', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('parentname', models.CharField(max_length=200)),
                ('parentnumber', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
    ]
