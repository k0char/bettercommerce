# Generated by Django 4.1.1 on 2022-10-16 19:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0006_listing_watchlist"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listing",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="listing",
            name="watchList",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="listingWatchlist",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
