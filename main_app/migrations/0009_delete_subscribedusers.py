# Generated by Django 4.1.4 on 2022-12-27 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0008_subscribedusers_alter_articles_image"),
    ]

    operations = [
        migrations.DeleteModel(
            name="SubscribedUsers",
        ),
    ]