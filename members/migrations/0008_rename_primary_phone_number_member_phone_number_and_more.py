# Generated by Django 4.1.7 on 2023-04-17 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_remove_member_profession'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='Primary_phone_number',
            new_name='Phone_number',
        ),
        migrations.RemoveField(
            model_name='member',
            name='Place_of_residence',
        ),
        migrations.RemoveField(
            model_name='member',
            name='Whatsapp_phone_number',
        ),
        migrations.RemoveField(
            model_name='member',
            name='Work_place',
        ),
        migrations.AddField(
            model_name='member',
            name='Wedding_anniversary',
            field=models.CharField(default='None', max_length=50),
        ),
    ]
