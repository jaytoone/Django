# Generated by Django 2.2.16 on 2020-12-22 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0021_message_recaptcha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='recaptcha',
            field=models.BooleanField(),
        ),
    ]