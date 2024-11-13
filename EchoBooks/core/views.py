
from .models import *
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout, authenticate,get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from . import forms
from django.db.models import Avg, Count
from collections import Counter
from math import floor
from django.utils import timezone


def index(request):
    return render(request, 'index.html')
def explore(request):
    return render(request, 'explore.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def home(request):
    return render(request, 'home.html')
def recent(request):
    return render(request, 'recent.html')
def save(request):
    return render(request, 'save.html')
def shop(request):
    return render(request, 'shop.html')
def settings(request):
    return render(request, 'settings.html')
def search(request):
    return render(request, 'search.html')
def about2(request):
    return render(request, 'about2.html')
def contact2(request):
    return render(request, 'contact2.html')
def activity(request):
    return render(request, 'activity.html')

def add_book(request):
    return render(request, 'add_book.html')
def admin_book(request):
    return render(request, 'admin_book.html')
def admin_books(request):
    return render(request, 'admin_books.html')
def admin_settings(request):
    return render(request, 'admin_settings.html')
def book(request,book_id):
    book = get_object_or_404(Book, id=book_id)
    profile = request.user.user_profile
    # Check if the book already exists in the user's recent books
    recent_book = RecentBook.objects.filter(profile=profile, book=book).first()
    is_saved = SavedBook.objects.filter(profile=profile, book=book).exists()
    if not recent_book:
        # If the book doesn't exist, create a new record
        RecentBook.objects.create(profile=profile, book=book)
    else:
        # If the book exists, update the viewed_date to the current date/time
        recent_book.viewed_date = timezone.now()
        recent_book.save()

    return render(request, 'book.html',{'book': book,'is_saved ':is_saved })
def dashboard(request):
    return render(request, 'dashboard.html')
def help(request):
    return render(request, 'help.html')
def notification(request):
    return render(request, 'notifications.html')
def privacy(request):
    return render(request, 'privacy.html')
def profile(request):
    return render(request, 'profile.html')
def read(request):
    return render(request, 'read.html')

def reviews(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    reviews = book.reviews.all()  # Use the correct related_name 'reviews'
    
    # Count the occurrences of each star rating
    star_counts = Counter([review.stars for review in reviews])
    
    # Calculate the overall rating as the average of all reviews
    total_reviews = len(reviews)
    if total_reviews > 0:
        overall_rating = sum([review.stars for review in reviews]) / total_reviews
    else:
        overall_rating = 0  # Default to 0 if no reviews
    star_percentages = {
        star: (star_counts.get(int(star), 0) * 100) / total_reviews if total_reviews > 0 else 0
        for star in "54321"
    }
    integer_rating = floor(overall_rating)
    decimal_rating = overall_rating - integer_rating
    context = {
        'book': book,
        'reviews': reviews,
        'star_counts': star_counts,
        'overall_rating': overall_rating,  # Add the overall rating to context
        'total_reviews': total_reviews,    # Add the total reviews to context
        'star_percentages': star_percentages,
        'integer_rating': integer_rating,
        'decimal_rating': decimal_rating,
    }
    return render(request, 'reviews.html', context)
def terms(request):
    return render(request, 'terms.html')
def users(request):
    return render(request, 'users.html')
@login_required
def write_review(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        rating = int(request.POST.get("rating"))
        content = request.POST.get("content")

        # Save the new review
        Review.objects.create(
            user=request.user,
            book=book,
            stars=rating,
            content=content
        )

        return redirect('book_reviews', book_id=book.id)

    return render(request, 'write_review.html', {'book': book})
def checkout(request):
    return render(request, 'checkout.html')

def signup(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            return JsonResponse({'error': 'Passwords do not match'}, status=400)
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "Username already exists."}, status=400)

        try:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            login(request, user)
            return JsonResponse({"success": True, "redirect_url": "/home/"})
        except Exception as e:
            return JsonResponse({"error": f"Error creating user: {str(e)}"}, status=400)

    return render(request, 'login.html')

def login_view(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('home')
        else:
            return JsonResponse({"error": "Invalid Username or Password."}, status=400)
    return render(request, 'login.html')
def logout_view(request):
    logout(request)
    return redirect('login')
@csrf_exempt
def check_password(request):
    if request.method == "POST":
        entered_password = request.POST.get('currentPassword')  # Get the entered password
        user = request.user  # Assuming the user is logged in
        if user.check_password(entered_password):  # Check the password
            return JsonResponse({'valid': True})
        else:
            return JsonResponse({'valid': False})
    return JsonResponse({'valid': False})
@login_required
def account(request):
    return render(request, 'account.html')


User = get_user_model()

@login_required
def get_user_info(request):
    user = request.user
    return JsonResponse({
        "username": user.username,
        "email": user.email
    })

@csrf_exempt
@login_required
def update_user_info(request):
    if request.method == "POST":
        user = request.user
        username = request.POST.get("username", user.username)
        email = request.POST.get("email", user.email)
        password = request.POST.get("password")
        
        # Update user fields if they were changed
        if username and username != user.username:
            user.username = username
        if email and email != user.email:
            user.email = email
        if password:
            user.set_password(password)
        
        # Save the user information
        user.save()

        # Check for a profile image and update if present
        if request.FILES.get('image'):
            profile, created = Profile.objects.get_or_create(user=user)
            profile.image = request.FILES['image']
            profile.save()

        return JsonResponse({"status": "success"})
    
    return JsonResponse({"status": "failed", "message": "Invalid request"}, status=400)
from django.http import JsonResponse
from .models import Review
from django.contrib.auth.decorators import login_required

@login_required
def like_review(request, review_id):
    if request.method == "POST":
        review = Review.objects.get(id=review_id)
        user = request.user

        # Implement logic to check if the user has already liked this review
        if user in review.liked_by.all():
            # User has already liked it, so "unlike" it
            review.likes -= 1
            review.liked_by.remove(user)
            liked = False
        else:
            # User has not liked it yet, so "like" it
            review.likes += 1
            review.liked_by.add(user)
            liked = True

        review.save()

        # Return the updated likes count and like status
        return JsonResponse({'likes': review.likes, 'liked': liked})

def submit_review(request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(Book, id=book_id)
        rating = int(request.POST.get('rating', 0))
        content = request.POST.get('content', '')

        if rating and content:
            review = Review.objects.create(user=request.user, book=book, stars=rating, content=content)
            review.save()
            messages.success(request, "Review added successfully!")
            return redirect('reviews', book_id=book_id)
        else:
            messages.error(request, "Unexpected error! Please try again.")
            return redirect('reviews', book_id=book_id)

def add_to_saved_books(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    profile = request.user.profile  # Get the current user's profile
    SavedBook.objects.create(profile=profile, book=book)
    return redirect('your_redirect_page')  # Redirect after adding (change as necessary)

@csrf_exempt
def save_book(request, book_id):
    if request.method == 'POST':
        book = Book.objects.get(id=book_id)
        profile = request.user.user_profile

        saved_book, created = SavedBook.objects.get_or_create(profile=profile, book=book)
        if not created:
            saved_book.delete()
            return JsonResponse({'saved': False})
        return JsonResponse({'saved': True})
    return JsonResponse({'error': 'Invalid request'}, status=400)
