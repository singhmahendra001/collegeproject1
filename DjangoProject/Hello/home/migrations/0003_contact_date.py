# Generated by Django 4.0.4 on 2022-04-23 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_contact_desc_alter_contact_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date',
            field=models.DateField(null=True),
        ),
    ]