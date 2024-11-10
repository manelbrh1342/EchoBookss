# Generated by Django 5.1.2 on 2024-11-10 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_remove_profile_recent_books_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='recent_books',
            field=models.ManyToManyField(blank=True, related_name='viewed_by_profiles', through='core.RecentBook', to='core.book'),
        ),
        migrations.AddField(
            model_name='profile',
            name='saved_books',
            field=models.ManyToManyField(blank=True, related_name='saved_by_profiles', through='core.SavedBook', to='core.book'),
        ),
    ]