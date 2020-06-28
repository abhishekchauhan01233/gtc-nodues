# Generated by Django 3.0.4 on 2020-06-28 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accounts',
            options={'verbose_name_plural': 'ACCOUNTS'},
        ),
        migrations.AlterModelOptions(
            name='exams',
            options={'verbose_name_plural': 'EXAMS'},
        ),
        migrations.AlterModelOptions(
            name='hod_1st_year',
            options={'verbose_name_plural': 'HOD 1ST YEAR'},
        ),
        migrations.AlterModelOptions(
            name='hod_auto',
            options={'verbose_name_plural': 'HOD AUTO'},
        ),
        migrations.AlterModelOptions(
            name='hod_civil',
            options={'verbose_name_plural': 'HOD CIVIL'},
        ),
        migrations.AlterModelOptions(
            name='hod_cse',
            options={'verbose_name_plural': 'HOD CSE'},
        ),
        migrations.AlterModelOptions(
            name='hod_ece',
            options={'verbose_name_plural': 'HOD ECE'},
        ),
        migrations.AlterModelOptions(
            name='hod_management',
            options={'verbose_name_plural': 'HOD MANAGEMENT'},
        ),
        migrations.AlterModelOptions(
            name='hod_me',
            options={'verbose_name_plural': 'HOD MECHANICAL'},
        ),
        migrations.AlterModelOptions(
            name='hostel',
            options={'verbose_name_plural': 'HOSTEL'},
        ),
        migrations.AlterModelOptions(
            name='library',
            options={'verbose_name_plural': 'LIBRARY'},
        ),
        migrations.AlterModelOptions(
            name='studentdata',
            options={'verbose_name_plural': 'STUDENT DATA'},
        ),
        migrations.AlterModelOptions(
            name='transport',
            options={'verbose_name_plural': 'TRANSPORT'},
        ),
    ]