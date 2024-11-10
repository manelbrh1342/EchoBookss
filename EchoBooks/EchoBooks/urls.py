from django.contrib import admin
from django.urls import path
from core import views  # Ensure to import your views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('explore/', views.explore, name='explore'),  # Removed leading slash
    path('about/', views.about, name='about'),        # Removed leading slash
    path('contact/', views.contact, name='contact'),  # Removed leading slash
    path('login/', views.login_view, name='login'),        # Removed leading slash
    path('signup/', views.signup, name='signup'), 
    path('home/', views.home, name='home'),            # Removed leading slash
    path('recent/', views.recent, name='recent'),      # Removed leading slash
    path('save/', views.save, name='save'),            # Removed leading slash
    path('search/', views.search, name='search'),      # Removed leading slash
    path('activity/', views.activity, name='activity'),  # Removed leading slash
    path('add_book/', views.add_book, name='add_book'),  # Add more paths as needed
    path('admin_book/', views.admin_book, name='admin_book'),
    path('admin_books/', views.admin_books, name='admin_books'),
    path('admin_settings/', views.admin_settings, name='admin_settings'),
    path('book/<int:book_id>/', views.book, name='book'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('help/', views.help, name='help'),
    path('/notification', views.notification, name='notification'),
    path('/privacy', views.privacy, name='privacy'),
    path('/profile', views.profile, name='profile'),
    path('/read', views.read, name='read'),
    path('book/<int:book_id>/reviews/', views.reviews, name='reviews'),
    path('/terms', views.terms, name='terms'),
    path('/users', views.users, name='users'),
    path('book/<int:book_id>/write-review/', views.write_review, name='write_review'),
    path('/shop',views.shop,name='shop'),
    path('/settings',views.settings,name='settings'),
    path('/checkout',views.checkout,name='checkout'),
    path('logout/', views.logout_view, name='logout'),
    path('account/',views.account,name='account'),
    path('contact2/', views.contact2,name='contact2'),
    path('about2/', views.about2,name='about2'),
    path('notification/', views.notification,name='notifications'),
    path('check-password/', views.check_password, name='check_password'),
    path('get_user_info/', views.get_user_info, name='get_user_info'),
    path('update_user_info/', views.update_user_info, name='update_user_info'),
    path('review/<int:review_id>/like/', views.like_review, name='like_review'),
    path('book/<int:book_id>/submit-review/', views.submit_review, name='submit_review'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
