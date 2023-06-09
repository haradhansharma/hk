# Generated by Django 4.1.7 on 2023-04-02 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_termsprivacysection_s_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmessage',
            name='in_workshops',
            field=models.ManyToManyField(related_name='contact_workshops', to='home.workshop'),
        ),
        migrations.AddField(
            model_name='contactmessage',
            name='interest_in',
            field=models.CharField(choices=[('donation', 'Donation'), ('volunteering', 'Volunteering')], default=1, max_length=20),
            preserve_default=False,
        ),
    ]
