# Generated by Django 2.2.2 on 2020-03-01 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generalzone', '0007_auto_20200301_1610'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentinfo',
            old_name='branch',
            new_name='nationality',
        ),
    ]
