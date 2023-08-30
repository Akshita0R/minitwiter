# Generated by Django 4.0.6 on 2022-08-17 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_tweet_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=200)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='media/profile_pics')),
            ],
        ),
    ]