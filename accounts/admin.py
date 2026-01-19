from django.contrib import admin
from .models import UserProfile  # Assuming you have a UserProfile model

admin.site.register(UserProfile)  # Register the UserProfile model with the admin site