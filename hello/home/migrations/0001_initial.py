# Generated by Django 4.0.6 on 2022-12-28 12:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Addbuilding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buildingname', models.CharField(max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=12)),
                ('desc', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Testing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_generated', models.FileField(blank=True, null=True, upload_to='profile/generated_files/')),
                ('newappname', models.CharField(default='', max_length=122)),
                ('newappphone', models.CharField(default='', max_length=12)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_user', models.FileField(blank=True, null=True, upload_to='profile/uploaded_files/')),
                ('file_generated', models.FileField(blank=True, null=True, upload_to='profile/generated_files/')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Newapp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newappname', models.CharField(max_length=122)),
                ('newappemail', models.CharField(max_length=122)),
                ('newappphone', models.CharField(max_length=12)),
                ('newappaddress', models.CharField(max_length=122)),
                ('newappdepart', models.CharField(max_length=255)),
                ('newappposition', models.CharField(max_length=255)),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Addroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomname', models.CharField(max_length=122)),
                ('invigilatorsinroom', models.ManyToManyField(blank=True, to='home.newapp')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Addexam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('examname', models.CharField(max_length=122)),
                ('examtype', models.CharField(max_length=122)),
                ('examsemtype', models.CharField(blank=True, max_length=122, null=True)),
                ('regularback', models.CharField(blank=True, max_length=122, null=True)),
                ('examcentre', models.CharField(max_length=122)),
                ('examdate', models.CharField(max_length=122)),
                ('newexamdate', models.DateField(blank=True, max_length=122, null=True)),
                ('examtime', models.CharField(max_length=122)),
                ('newexamtime', models.TimeField(blank=True, max_length=122, null=True)),
                ('examtime_end', models.CharField(blank=True, max_length=122, null=True)),
                ('newexamtime_end', models.TimeField(blank=True, max_length=122, null=True)),
                ('examdesc', models.TextField()),
                ('examaddbuilding', models.ManyToManyField(blank=True, to='home.addbuilding')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.profile')),
            ],
        ),
        migrations.AddField(
            model_name='addbuilding',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.profile'),
        ),
        migrations.AddField(
            model_name='addbuilding',
            name='rooms',
            field=models.ManyToManyField(blank=True, to='home.addroom'),
        ),
    ]