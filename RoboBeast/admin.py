from django.contrib import admin
from .models import *




@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'first_name', 'last_name', 'username', 'display_Image', 'description', 'city', 'address', 'phone', 'is_active')
    ordering = ['user_id']
    search_fields = ('user_id', 'first_name', 'last_name', 'username', 'display_Image', 'description', 'city', 'address', 'phone', 'is_active')
    list_display_links = ('user_id', 'first_name', 'last_name', 'username', 'display_Image', 'description', 'city', 'address', 'phone', 'is_active')
    fieldsets = (
        ('User Profile', {
            'fields': ('user_id', 'first_name', 'last_name', 'username', 'display_Image', 'description', 'city', 'address', 'phone', 'is_active')}),
    )
    list_per_page = 25

