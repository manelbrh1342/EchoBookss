from django.contrib import admin
from .models import *

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'priceDZD','priceUSD' ,'total_comments', 'total_stars', 'languages', 'number_of_pages', 'publication_date')
    search_fields = ('title', 'description')
    list_filter = ('genre', 'languages', 'publication_date')
    ordering = ('-publication_date',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'image')  # Display the user and profile picture in the list view
    search_fields = ('user__username', 'user__email')  # Allow searching by username or email
    list_filter = ('user__is_active', 'user__date_joined')  # Filter by active status and date joined
    ordering = ('user__date_joined',)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'stars', 'submission_date')  # Use 'user' and 'stars' directly
    list_filter = ('stars', 'submission_date')  # Use 'stars' for filtering

admin.site.register(Review, ReviewAdmin)

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'book', 'purchased_audio', 'purchased_pdf', 'purchase_date')
    list_filter = ('purchased_audio', 'purchased_pdf', 'purchase_date')

    def get_username(self, obj):
        return obj.profile.user.username
    get_username.short_description = 'User'

admin.site.register(Purchase, PurchaseAdmin)
@admin.register(SavedBook)
class SavedBookAdmin(admin.ModelAdmin):
    list_display = ('profile', 'book', 'added_date')  # Add the fields you want to display
    search_fields = ('profile__user__username', 'book__title')  # Optional: Add search fields
    list_filter = ('profile',)  # Optional: Add filters

# Register RecentBook model
@admin.register(RecentBook)
class RecentBookAdmin(admin.ModelAdmin):
    list_display = ('profile', 'book', 'viewed_date')  # Add the fields you want to display
    search_fields = ('profile__user__username', 'book__title')  # Optional: Add search fields
    list_filter = ('profile',)  # Optional: Add filters