from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.conf import settings
from django.utils import timezone
def image_upload(instance,filename):
    imagename ,extension = filename.split(".")
    return "profilePicture/%s.%s"%(instance.id,extension)#we used the id instead of a normal name because dealing with numbers is easier and faster for django 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    image = models.ImageField(upload_to=image_upload)
    purchased_books = models.ManyToManyField(
        'Book',
        through='Purchase',
        related_name='purchased_by_profiles',
        blank=True
    )
    def __str__(self):
        return str(self.user)
    def saved_books(self):
        return SavedBook.objects.filter(profile=self)

    def recent_books(self):
        return RecentBook.objects.filter(profile=self)


class Book(models.Model):
    GENRE_CHOICES = [
        ('Fiction', 'Fiction'),
        ('Non-Fiction', 'Non-Fiction'),
        ('Mystery', 'Mystery'),
        ('Sci-fi', 'Science Fiction'),
        ('Fantasy', 'Fantasy'),
        # Add more genres as needed
    ]
    
    LANGUAGE_CHOICES = [
        ('EN', 'English'),
        ('FR', 'French'),
        ('AR', 'Arabic'),
        ('SP', 'Spanish'),
        ('IT', 'Italian'),
        ('CH', 'Chinese'),
        # Add more languages as needed
    ]
    # Basic Info
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    description = models.TextField()
    languages = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)
    publication_date = models.DateField()
    
    # Media
    content = models.FileField(upload_to='books/content_pdfs/', blank=True, null=True)  # PDF content
    audio_version = models.FileField(upload_to='books/audio_versions/', blank=True, null=True)  # MP3 audio
    cover_image = models.ImageField(upload_to='books/cover_images/', blank=True, null=True)
    
    # Pricing and Ratings
    priceDZD = models.DecimalField(max_digits=10, decimal_places=2)
    priceUSD = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    total_comments = models.PositiveIntegerField(default=0)
    total_stars = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)  # Average rating

    # Additional Info
    number_of_pages = models.PositiveIntegerField()
    audio_length = models.DurationField()  # Use timedelta for length of audio

    
    def __str__(self):
        return self.title


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Link to user
    book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)  # Link to book
    content = models.TextField()
    stars = models.PositiveSmallIntegerField()  # Rating out of 5, for example
    likes = models.PositiveIntegerField(default=0)
    submission_date = models.DateTimeField(default=timezone.now)
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="liked_reviews", blank=True)
    def __str__(self):
        return f"Review by {self.user.username} for {self.book.title}"

    def save(self, *args, **kwargs):
        # Update the total stars in the associated Book instance
        if self.pk is None:  # Check if it's a new review
            total_reviews = self.book.reviews.count()
            current_total_stars = self.book.total_stars * total_reviews
            self.book.total_stars = (current_total_stars + self.stars) / (total_reviews + 1)
            self.book.save(update_fields=['total_stars'])
        super().save(*args, **kwargs)

class Purchase(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    purchased_audio = models.BooleanField(default=False)
    purchased_pdf = models.BooleanField(default=False)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.profile.user.username} purchased {self.book.title}"

class SavedBook(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.profile.user.username} saved {self.book.title}"

class RecentBook(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    viewed_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.profile.user.username} viewed {self.book.title}"
