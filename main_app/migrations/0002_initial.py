# Generated by Django 4.1.4 on 2023-01-02 11:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("main_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="articleseries",
            name="author",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="articles",
            name="author",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="articles",
            name="series",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.SET_DEFAULT,
                to="main_app.articleseries",
                verbose_name="Series",
            ),
        ),
    ]
